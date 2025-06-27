-- Pull in the wezterm API
local wezterm = require("wezterm")

-- This will hold the configuration.
local config = wezterm.config_builder()

-- Spawn a fish shell in login mode
config.default_prog = { "fish" }

-- Font
config.font = wezterm.font("Iosevka Nerd Font Mono")

-- Theme
config.color_scheme = "Catppuccin Latte"

-- Background
config.window_background_opacity = 0.64

-- and finally, return the configuration to wezterm
return config
