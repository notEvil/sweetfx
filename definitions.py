# effect names
ASCII = "ASCII.fx"
Bloom = "Bloom.fx"
Border = "Border.fx"
CRT = "CRT.fx"
Cartoon = "Cartoon.fx"
ChromaticAberration = "ChromaticAberration.fx"
ColorMatrix = "ColorMatrix.fx"
Curves = "Curves.fx"
DPX = "DPX.fx"
Daltonize = "Daltonize.fx"
DisplayDepth = "DisplayDepth.fx"
FXAA = "FXAA.fx"
FakeHDR = "FakeHDR.fx"
FilmGrain = "FilmGrain.fx"
Levels = "Levels.fx"
LiftGammaGain = "LiftGammaGain.fx"
LumaSharpen = "LumaSharpen.fx"
Monochrome = "Monochrome.fx"
Nostalgia = "Nostalgia.fx"
SMAA = "SMAA.fx"
Sepia = "Sepia.fx"
Splitscreen = "Splitscreen.fx"
Technicolor = "Technicolor.fx"
Technicolor2 = "Technicolor2.fx"
Tonemap = "Tonemap.fx"
Vibrance = "Vibrance.fx"
Vignette = "Vignette.fx"

effect_name_by_use = {
    "USE_ADVANCED_CRT": CRT,
    "USE_ASCII": ASCII,
    "USE_BLOOM": Bloom,
    "USE_BORDER": Border,
    "USE_CA": ChromaticAberration,
    "USE_CARTOON": Cartoon,
    "USE_COLORMATRIX": ColorMatrix,
    "USE_CURVES": Curves,
    "USE_DISPLAY_DEPTH": DisplayDepth,
    "USE_DPX": DPX,
    "USE_FILMGRAIN": FilmGrain,
    "USE_FXAA": FXAA,
    "USE_HDR": FakeHDR,
    "USE_LEVELS": Levels,
    "USE_LIFTGAMMAGAIN": LiftGammaGain,
    "USE_LUMASHARPEN": LumaSharpen,
    "USE_MONOCHROME": Monochrome,
    "USE_NOSTALGIA": Nostalgia,
    "USE_SEPIA": Sepia,
    "USE_SMAA": SMAA,
    "USE_SPLITSCREEN": Splitscreen,
    "USE_TECHNICOLOR": Technicolor,
    "USE_TECHNICOLOR2": Technicolor2,
    "USE_TONEMAP": Tonemap,
    "USE_VIBRANCE": Vibrance,
    "USE_VIGNETTE": Vignette,
}


class ReshadeParameterTarget:
    def __init__(self, effect_name, parameter_name, parameter_index=None):
        self.effect_name = effect_name
        self.parameter_name = parameter_name
        self.parameter_index = parameter_index


T = ReshadeParameterTarget

# TODO
# - Reshade defines
#   ? assert
reshade_parameter_target_by_reshade_define_name = {
    "Ascii_background_color": T(ASCII, "Ascii_background_color"),
    "Ascii_font": T(ASCII, "Ascii_font"),
    "Ascii_font_color": T(ASCII, "Ascii_font_color"),
    "Ascii_font_color_mode": T(ASCII, "Ascii_font_color_mode"),
    "Ascii_input_image": T(ASCII, None),
    "Ascii_invert_brightness": T(ASCII, "Ascii_invert_brightness"),
    "Ascii_spacing": T(ASCII, "Ascii_spacing"),
    "Ascii_swap_colors": T(ASCII, "Ascii_swap_colors"),
    "Bleach": T(Tonemap, "Bleach"),
    "Blend": T(DPX, "Strength"),
    "BloomPower": T("Bloom", None),
    "BloomThreshold": T("Bloom", None),
    "BloomWidth": T("Bloom", None),
    "Blue": T(DPX, "RGB_Curve", parameter_index=2),
    "BlueC": T(DPX, "RGB_C", parameter_index=2),
    "CRTAmount": T(CRT, "Amount"),
    "CRTAngleX": T(CRT, "Angle", parameter_index=0),
    "CRTAngleY": T(CRT, "Angle", parameter_index=1),
    "CRTBrightness": T(CRT, "Brightness"),
    "CRTCornerSize": T(CRT, "CornerSize"),
    "CRTCurvature": T(CRT, "Curvature"),
    "CRTCurvatureRadius": T(CRT, "CurvatureRadius"),
    "CRTDistance": T(CRT, "ViewerDistance"),
    "CRTOverScan": T(CRT, "Overscan"),
    "CRTOversample": T(CRT, "Oversample"),
    "CRTResolution": T(CRT, "Resolution"),
    "CRTScanlineGaussian": T(CRT, "ScanlineGaussian"),
    "CRTScanlineIntensity": T(CRT, "ScanlineIntensity"),
    "CRTgamma": T(CRT, "Gamma"),
    "CRTmonitorgamma": T(CRT, "MonitorGamma"),
    "CartoonEdgeSlope": T(Cartoon, "EdgeSlope"),
    "CartoonPower": T(Cartoon, "Power"),
    "Chromatic_shift": T(ChromaticAberration, "Shift"),
    "Chromatic_strength": T(ChromaticAberration, "Strength"),
    "ColorGamma": T(DPX, "ColorGamma"),
    "ColorMatrix_Blue": T(ColorMatrix, "ColorMatrix_Blue"),
    "ColorMatrix_Green": T(ColorMatrix, "ColorMatrix_Green"),
    "ColorMatrix_Red": T(ColorMatrix, "ColorMatrix_Red"),
    "ColorMatrix_strength": T(ColorMatrix, "Strength"),
    "ColorTone": T(Sepia, "Tint"),
    "Curves_contrast": T(Curves, "Contrast"),
    "Curves_formula": T(Curves, "Formula"),
    "Curves_mode": T(Curves, "Mode"),
    "DPXSaturation": T(DPX, "Saturation"),
    "Daltonize_type": T(Daltonize, "Type"),
    "Defog": T(Tonemap, "Defog"),
    "Depth_z_far": T("Display", None),
    "Depth_z_near": T("Display", None),
    "Explosion_Radius": T("Explosion", None),
    "Exposure": T(Tonemap, "Exposure"),
    "FXAA_QUALITY__PRESET": T(FXAA, None),
    "FilmGrain_SNR": T(FilmGrain, "SignalToNoiseRatio"),
    "FilmGrain_intensity": T(FilmGrain, "Intensity"),
    "FilmGrain_mean": T(FilmGrain, "Mean"),
    "FilmGrain_variance": T(FilmGrain, "Variance"),
    "FogColor": T(Tonemap, "FogColor"),
    "Gamma": T(Tonemap, "Gamma"),
    "Green": T(DPX, "RGB_Curve", parameter_index=1),
    "GreenC": T(DPX, "RGB_C", parameter_index=1),
    "GreyPower": T(Sepia, None),
    "HDRPower": T(FakeHDR, "HDRPower"),
    "Levels_black_point": T(Levels, "BlackPoint"),
    "Levels_highlight_clipping": T(Levels, "HighlightClipping"),
    "Levels_white_point": T(Levels, "WhitePoint"),
    "Monochrome_color_saturation": T(Monochrome, "Monochrome_color_saturation"),
    "Monochrome_conversion_values": T(Monochrome, "Monochrome_conversion_values"),
    "PixelArtCRT_ShadowMask": T("Pixel-Art CRT", None),
    "PixelArtCRT_fixed_resolution": T("Pixel-Art CRT", None),
    "PixelArtCRT_hardPix": T("Pixel-Art CRT", None),
    "PixelArtCRT_hardScan": T("Pixel-Art CRT", None),
    "PixelArtCRT_maskDark": T("Pixel-Art CRT", None),
    "PixelArtCRT_maskLight": T("Pixel-Art CRT", None),
    "PixelArtCRT_overdrive": T("Pixel-Art CRT", None),
    "PixelArtCRT_resolution_mode": T("Pixel-Art CRT", None),
    "PixelArtCRT_resolution_ratio": T("Pixel-Art CRT", None),
    "PixelArtCRT_shape": T("Pixel-Art CRT", None),
    "PixelArtCRT_warp": T("Pixel-Art CRT", None),
    "RGB_Gain": T(LiftGammaGain, "RGB_Gain"),
    "RGB_Gamma": T(LiftGammaGain, "RGB_Gamma"),
    "RGB_Lift": T(LiftGammaGain, "RGB_Lift"),
    "Red": T(DPX, "RGB_Curve", parameter_index=0),
    "RedC": T(DPX, "RGB_C", parameter_index=0),
    "SMAA_CORNER_ROUNDING": T(SMAA, "CornerRounding"),
    "SMAA_DEBUG_OUTPUT": T(SMAA, "DebugOutput"),
    "SMAA_DEPTH_THRESHOLD": T(SMAA, None),
    "SMAA_DIRECTX9_LINEAR_BLEND": T(SMAA, None),
    "SMAA_EDGE_DETECTION": T(SMAA, "EdgeDetectionType"),
    "SMAA_MAX_SEARCH_STEPS": T(SMAA, "MaxSearchSteps"),
    "SMAA_MAX_SEARCH_STEPS_DIAG": T(SMAA, "MaxSearchStepsDiagonal"),
    "SMAA_PREDICATION": T(SMAA, None),
    "SMAA_PREDICATION_SCALE": T(SMAA, "PredicationScale"),
    "SMAA_PREDICATION_STRENGTH": T(SMAA, "PredicationStrength"),
    "SMAA_PREDICATION_THRESHOLD": T(SMAA, "PredicationThreshold"),
    "SMAA_THRESHOLD": T(SMAA, "EdgeDetectionThreshold"),
    "Saturation": T(Tonemap, "Saturation"),
    "SepiaPower": T(Sepia, "Strength"),
    "TechniAmount": T(Technicolor, "Strength"),
    "TechniPower": T(Technicolor, "Power"),
    "Technicolor2_Blue_Strength": T(Technicolor2, "ColorStrength", parameter_index=2),
    "Technicolor2_Brightness": T(Technicolor2, "Brightness"),
    "Technicolor2_Green_Strength": T(Technicolor2, "ColorStrength", parameter_index=1),
    "Technicolor2_Red_Strength": T(Technicolor2, "ColorStrength", parameter_index=0),
    "Technicolor2_Saturation": T(Technicolor2, "Saturation"),
    "Technicolor2_Strength": T(Technicolor2, "Strength"),
    "Transition_texture": T("Transition", None),
    "Transition_texture_height": T("Transition", None),
    "Transition_texture_width": T("Transition", None),
    "Transition_time": T("Transition", None),
    "Transition_type": T("Transition", None),
    "Vibrance": T(Vibrance, "Vibrance"),
    "Vibrance_RGB_balance": T(Vibrance, "VibranceRGBBalance"),
    "VignetteAmount": T(Vignette, "Amount"),
    "VignetteCenter": T(Vignette, "Center"),
    "VignetteRadius": T(Vignette, "Radius"),
    "VignetteRatio": T(Vignette, "Ratio"),
    "VignetteSlope": T(Vignette, "Slope"),
    "VignetteType": T(Vignette, "Type"),
    "blueNegativeAmount": T(Technicolor, "RGBNegativeAmount", parameter_index=2),
    "border_color": T(Border, "border_color"),
    "border_ratio": T(Border, "border_ratio"),
    "border_width": T(Border, "border_width"),
    "custom_strength": T("Custom", None),
    "dither_method": T("Dither", None),
    "fxaa_EdgeThreshold": T(FXAA, "EdgeThreshold"),
    "fxaa_EdgeThresholdMin": T(FXAA, "EdgeThresholdMin"),
    "fxaa_Subpix": T(FXAA, "Subpix"),
    "greenNegativeAmount": T(Technicolor, "RGBNegativeAmount", parameter_index=1),
    "offset_bias": T(LumaSharpen, "offset_bias"),
    "pattern": T(LumaSharpen, "pattern"),
    "radius2": T(FakeHDR, "radius2"),
    "redNegativeAmount": T(Technicolor, "RGBNegativeAmount", parameter_index=0),
    "sharp_clamp": T(LumaSharpen, "sharp_clamp"),
    "sharp_strength": T(LumaSharpen, "sharp_strength"),
    "show_sharpen": T(LumaSharpen, "show_sharpen"),
    "splitscreen_mode": T(Splitscreen, "splitscreen_mode"),
}


techniques_by_effect_name = {
    CRT: ["AdvancedCRT"],
    ASCII: ["ASCII"],
    Bloom: ["BloomAndLensFlares"],
    Border: ["Border"],
    ChromaticAberration: ["CA"],
    Cartoon: ["Cartoon"],
    ColorMatrix: ["ColorMatrix"],
    Curves: ["Curves"],
    DisplayDepth: ["DisplayDepth"],
    DPX: ["DPX"],
    FilmGrain: ["FilmGrain"],
    FXAA: ["FXAA"],
    FakeHDR: ["HDR"],
    Levels: ["Levels"],
    LiftGammaGain: ["LiftGammaGain"],
    LumaSharpen: ["LumaSharpen"],
    Monochrome: ["Monochrome"],
    Nostalgia: ["Nostalgia"],
    Sepia: ["Tint"],
    SMAA: ["SMAA"],
    Splitscreen: ["Before", "After"],
    Technicolor: ["Technicolor"],
    Technicolor2: ["Technicolor2"],
    Tonemap: ["Tonemap"],
    Vibrance: ["Vibrance"],
    Vignette: ["Vignette"],
}
