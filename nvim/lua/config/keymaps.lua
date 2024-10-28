-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here
--
-- TODO:
-- Avoir f directement dans nvim
-- avoir un truc qui run le fichier que ce soit en python, en rust ou sh ? -> en vrai juste utiliser un terminal à côté

-- Celui que tu utilises le plus
vim.keymap.set("i", "<leader><leader>", "<Esc>")

-- On les remets en nvi parce qu'on pouvait le faire que en normal avant
-- vim.keymap.set({ "n", "v", "i" }, "<C-h>", "<C-w>h")
-- vim.keymap.set({ "n", "v", "i" }, "<C-j>", "<C-w>j")
-- vim.keymap.set({ "n", "v", "i" }, "<C-k>", "<C-w>k")
-- vim.keymap.set({ "n", "v", "i" }, "<C-l>", "<C-w>l")
-- Mdr ça marche pas dommage

-- On rajoute celui où on peut déplacer
vim.keymap.set({ "n", "v", "i" }, "<C-S-h>", "<C-w><S-h>")
vim.keymap.set({ "n", "v", "i" }, "<C-S-j>", "<C-w><S-j>")
vim.keymap.set({ "n", "v", "i" }, "<C-S-k>", "<C-w><S-k>")
vim.keymap.set({ "n", "v", "i" }, "<C-S-l>", "<C-w><S-l>")

-- Les keymaps pour changer de buffers
vim.keymap.set("n", "<leader>h", ":BufferLineCyclePrev<CR>", { silent = true })
vim.keymap.set("n", "<leader>l", ":BufferLineCycleNext<CR>", { silent = true })
vim.keymap.set("n", "<leader><S-h>", ":BufferLineMovePrev<CR>", { silent = true })
vim.keymap.set("n", "<leader><S-l>", ":BufferLineMoveNext<CR>", { silent = true })
-- Supprimer le buffer
vim.keymap.set("n", "<leader>dd", ":lua require('mini.bufremove').delete()<CR>", { silent = true })

-- Les keymaps pour les splits
local wk = require("which-key")
wk.register({
  v = {
    name = "splits",
    h = { ":vsplit<CR><C-w>h", "Right-side not focused window", silent = true },
    j = { ":split<CR>", "Bottom focused window", silent = true },
    k = { ":split<CR><C-w>k", "Bottom not focused window", silent = true },
    l = { ":vsplit<CR>", "Right-side focused window", silent = true },
    d = { ":q<CR>", "Delete window", silent = true },
  },
}, { prefix = "<leader>" })

-- On désactive TAB dans LuaSnip pour avoir TAB pour la completion
-- Plus besoin : il y a plus LuaSnip
