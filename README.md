# Sweetfx 2.0 to Reshade 4 converter

This python script tries to convert Sweetfx (version 2.0) presets to Reshade (version 4) configurations.
It is not perfect, so it might not work out-of-the-box for your specific preset or produce undesired results.
In certain cases a slight modification is sufficient to make it work, so just open an issue if you think this is the case.
Hope it's useful for some!

## What it does

- Reads Sweetfx preset from stdin
- Parses input using grammar
- Traverses parsed tree and extracts information
- Assembles Reshade configuration
- Writes to stdout and logs to stderr

## What it assumes

- Mapping between Sweetfx defines and Reshade effects, techniques and attributes is correct
- Transformations are correct
  - Division in python yields equal result to division in HLSL
  - `float2` is array of 2 floats
  - `float3` is array of 3 floats
- Values still mean the same
- Defines in Reshade effects can be ignored
- Syntax of Reshade configuration is correct
- Type casts are allowed
  - Mostly integer value to boolean variable

## What it depends on

- lark

## How to run it

- install python 3
- install lark for python 3
- run convert.py with python 3, pipe Sweetfx preset to stdin and stdout to some file
  - in bash this would be similar to `python3 convert.py < /path/to/Sweetfx.preset.file 1> /path/to/Reshade.configuration.file`
