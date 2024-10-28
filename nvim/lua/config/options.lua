-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here
vim.g.mapleader = ","
vim.g.maplocalleader = ","

-- Si ça marche je casse la tête à folke même si c'est le goat
-- Ça marche putain c'est un truc de fou comment c'était caché
vim.g.autoformat = false

vim.opt.clipboard = "unnamed"
vim.opt.cursorline = false
vim.opt.scrolloff = 3
-- vim.opt.signcolumn = "auto"
vim.opt.wrap = true
vim.opt.whichwrap = "h,l,[,]"
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.timeoutlen = 500
vim.opt.shiftwidth = 4
vim.opt.smarttab = true
vim.opt.expandtab = true
vim.opt.tabstop = 4

vim.g.tutor_is_loaded = 1

-- Pour les fichiers de config de hyprland
vim.filetype.add({
  pattern = { [".*/hypr/.*%.conf"] = "hyprlang" },
})
