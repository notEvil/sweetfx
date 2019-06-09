import definitions
import functions
import lark
import argparse
import collections
import logging
import re
import sys


GRAMMAR = """
start: (define | comment1 | comment2 | NEWLINE)*
define: "#define" name expression
name: /[a-zA-Z_][a-zA-Z0-9_]*/
expression: number | string | division | brackets | function
number: /-?\d+(\.\d+)?/
string: /".*?(?<!\\\\)"/ | name
division: expression "/" expression
brackets: "(" expression ")"
function: name "(" expression ("," expression)* ")"
comment1: "//" /.+/?
comment2: "/*" /.*?\*\//s
%ignore " "
%ignore "\\t"
%import common.NEWLINE
"""


class Transformer(lark.Transformer):
    def __init__(self):
        self.used_effect_names = []
        self.unknown_uses = {}
        self.parameters_by_effect_name = {}
        self.unused_defines_by_effect_name = {}
        self.any_warning = False

    def start(self, children):
        pass

    def define(self, children):
        name, value = children

        if name.startswith("USE_"):
            effect_name = definitions.effect_name_by_use.get(name, None)

            if effect_name is None:
                self.unknown_uses[name] = bool(evaluate(value))
                return

            if evaluate(value) == 0:
                return

            self.used_effect_names.append(effect_name)
            return

        reshade_parameter_target = definitions.reshade_parameter_target_by_reshade_define_name.get(
            name, None
        )
        if reshade_parameter_target is not None:
            if reshade_parameter_target.parameter_name is None:
                self.unused_defines_by_effect_name.setdefault(
                    reshade_parameter_target.effect_name, {}
                )[name] = value
                return

            parameters = self.parameters_by_effect_name.setdefault(
                reshade_parameter_target.effect_name, {}
            )

            if reshade_parameter_target.parameter_index is None:
                parameters[reshade_parameter_target.parameter_name] = value

            else:
                values = parameters.setdefault(
                    reshade_parameter_target.parameter_name, Array()
                )
                self._ensure_capacity(
                    values, reshade_parameter_target.parameter_index + 1
                )
                values[reshade_parameter_target.parameter_index] = value

            return

        logging.warning("unused define: {} = {}".format(name, value))
        self.any_warning = True

    def _ensure_capacity(self, x, length):
        x.extend(None for _ in range(length - len(x)))

    def expression(self, children):
        result, = children
        return result

    def function(self, children):
        name = children[0]

        str_ = lambda: "{}({})".format(
            children[0], ", ".join(str(expression) for expression in children[1:])
        )

        if name == "float":

            def evaluate_():
                expression, = children[1:]
                value = evaluate(expression)
                result = float(value)
                return result

            result = Expression(str_, evaluate_)
            return result

        if name in ["float2", "float3"]:
            n = 2 if name == "float2" else 3

            def evaluate_():
                expressions = children[1:]
                assert len(expressions) == n
                result = Array(
                    float(evaluate(expression)) for expression in expressions
                )
                return result

            result = Expression(str_, evaluate_)
            return result

        result = Expression(
            str_,
            lambda: getattr(functions, children[0])(
                [evaluate(child) for child in children[1:]]
            ),
        )
        return result

    def division(self, children):
        numerator, denominator = children
        result = Expression(
            lambda: "{} / {}".format(numerator, denominator),
            lambda: evaluate(numerator) / evaluate(denominator),
        )
        return result

    def brackets(self, children):
        expression, = children
        result = Expression(
            lambda: "({})".format(expression), lambda: evaluate(expression)
        )
        return result

    def name(self, children):
        token, = children
        result = token.value
        return result

    def number(self, children):
        token, = children
        value = token.value
        # result = float(result) if '.' in result else int(result)
        result = Expression(
            lambda: value, lambda: (float if "." in value else int)(value)
        )
        return result

    def string(self, children):
        result, = children
        if isinstance(result, lark.Token):
            result = result.value
        else:
            result = '"{}"'.format(result)
        return result

    def comment1(self, children):
        pass

    def comment2(self, children):
        pass

    def __default__(self, data, children, meta):
        raise NotImplementedError(data)


class Expression:
    def __init__(self, str_function, evaluate_function):
        self.str_function = str_function
        self.evaluate_function = evaluate_function

    def evaluate(self):
        result = self.evaluate_function()
        return result

    def __str__(self):
        result = self.str_function()
        return result

    def __repr__(self):
        result = str(self)
        return result


class Array(list, Expression):
    def __init__(self, items=None):
        list.__init__(self, [] if items is None else items)
        Expression.__init__(self, self._str, self._evaluate)

    def _evaluate(self):
        result = Array(evaluate(value) for value in self)
        return result

    def _str(self):
        result = ",".join(str(value) for value in self)
        return result


def evaluate(x):
    if isinstance(x, Expression):
        result = x.evaluate()
        return result

    return x


logging.basicConfig(level="INFO")

# parse arguments
parser = argparse.ArgumentParser()

parser.parse_args()
#

parser = lark.Lark(GRAMMAR)
tree = parser.parse(sys.stdin.read())

transformer = Transformer()
transformer.transform(tree)

any_warning = False

if len(transformer.unknown_uses) != 0:
    unknown_uses = {name for name, used in transformer.unknown_uses.items() if used}
    if len(unknown_uses):
        logging.warning("unknown uses: {}".format(repr(unknown_uses)))
        any_warning = True

    unknown_uses = {name for name, used in transformer.unknown_uses.items() if not used}
    if len(unknown_uses):
        logging.info("unknown uses: {}".format(repr(unknown_uses)))


print("Effects", "=", ",".join(sorted(transformer.used_effect_names)), sep="")

all_techniques = []
for effect_name in transformer.used_effect_names:
    techniques = definitions.techniques_by_effect_name.get(effect_name, [])

    if 1 < len(techniques):
        logging.warning(
            "multiple techniques for effect {}; might need disabling; techniques: {}".format(
                repr(effect_name), repr(techniques)
            )
        )
        any_warning = True

    all_techniques.extend(techniques)

print("Techniques", "=", ",".join(all_techniques), sep="")
print("TechniqueSorting", "=", ",".join(all_techniques), sep="")

for effect_name in sorted(
    transformer.parameters_by_effect_name.keys()
    | transformer.unused_defines_by_effect_name.keys()
):
    print()
    print("[", effect_name, "]", sep="")

    used = effect_name in transformer.used_effect_names
    parameters = transformer.parameters_by_effect_name.get(effect_name, {})
    unused_defines = transformer.unused_defines_by_effect_name.get(effect_name, [])

    if len(unused_defines) != 0:
        if len(parameters) == 0:
            (logging.warning if used else logging.info)(
                "unused effect {}; defines: {}".format(
                    repr(effect_name), repr(unused_defines)
                )
            )
            any_warning |= used

        else:
            (logging.warning if used else logging.info)(
                "unused defines for effect {}; possibly kills effect; defines: {}".format(
                    repr(effect_name), repr(unused_defines)
                )
            )
            any_warning |= used

    for name, value in parameters.items():
        print(name, "=", evaluate(value), sep="")

if any_warning:
    logging.warning("finished with warnings")
