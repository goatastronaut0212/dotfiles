-- Pull in the wezterm API
local wezterm = require 'wezterm'

-- This will hold the configuration.
local config = wezterm.config_builder()

-- Spawn a fish shell in login mode
config.default_prog = { 'fish' }

-- Font
config.font = wezterm.font('Iosevka Nerd Font Mono')

-- and finally, return the configuration to wezterm
return config
