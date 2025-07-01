---------------------
-- PACKAGE MANAGER --
---------------------
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not (vim.uv or vim.loop).fs_stat(lazypath) then
  local lazyrepo = "https://github.com/folke/lazy.nvim.git"
  local out = vim.fn.system({ "git", "clone", "--filter=blob:none", "--branch=stable", lazyrepo, lazypath })
  if vim.v.shell_error ~= 0 then
    vim.api.nvim_echo({
      { "Failed to clone lazy.nvim:\n", "ErrorMsg" },
      { out, "WarningMsg" },
      { "\nPress any key to exit..." },
    }, true, {})
    vim.fn.getchar()
    os.exit(1)
  end
end
vim.opt.rtp:prepend(lazypath)

-- Ne pas oublier le ":" après le keyword
-- FIX: fix
-- TODO: todo
-- HACK: hack
-- WARN: warn
-- PERF: perf
-- NOTE: note
-- TEST: test

------------------
-- VIM SETTINGS --
------------------
vim.filetype.add {
  extension = { rasi = 'rasi' },
  pattern = {
    ['.*/waybar/config'] = 'jsonc',
    ['.*/mako/config'] = 'dosini',
    ['.*/kitty/*.conf'] = 'bash',
    ['.*/hypr/.*%.conf'] = 'hyprlang',
  }
}

-- Sinon tu dois taper 2 fois entrer pour sortir de nvim
vim.g.loaded_netrw = 0
vim.g.loaded_netrwPlugin = 0

vim.opt.listchars = { trail = "~", nbsp = "␣", tab = "  "}
vim.opt.list = true

vim.opt.shortmess:append("F")

vim.g.hlsearch = false
vim.g.mapleader = ","
vim.g.maplocalleader = ","
vim.opt.termguicolors = true

vim.g.showcmd = true
vim.g.autoformat = false

vim.opt.clipboard = "unnamedplus"
vim.opt.cursorline = false
vim.opt.scrolloff = 4
vim.opt.signcolumn = "auto"
vim.opt.number = true
vim.opt.relativenumber = true

vim.opt.undofile = true
vim.opt.undolevels = 1000
vim.opt.undodir = vim.fn.expand("~/.cache/nvim/undo")

vim.opt.wrap = true
vim.opt.whichwrap = "h,l,[,]"
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.timeoutlen = 500

vim.opt.expandtab = true
vim.opt.tabstop = 2
vim.opt.softtabstop = 2
vim.opt.shiftwidth = 2

vim.g.tutor_is_loaded = 1

-- Essentiel : affiche les textes virtuels (pour les msg d'erreur)
-- vim.diagnostic.config({ virtual_lines = true })
vim.diagnostic.config({ virtual_text = true })

-- Pour les fichiers de config de hyprland
vim.filetype.add({
  pattern = { [".*/hypr/.*%.conf"] = "hyprlang" },
})

-- Pour revenir à l'ancienne position (vraiment cool)
vim.api.nvim_create_autocmd({ "BufReadPost" }, {
  pattern = { "*" },
  callback = function()
    vim.api.nvim_exec('silent! normal! g`"zv', false)
  end
})


-- Askip indent-blankline s'en occupe
-- Finalement indent-blankline ne fait pas le poids face à mini.indentscope
-- En fait on installe les 2 ez
-- OK indent-blankline ne retire pas du tout ça
vim.api.nvim_create_autocmd({ "BufWritePre" }, {
  pattern = { "*" },
  callback = function()
    vim.api.nvim_exec(':%s/\\s\\+$//e', false)
  end
})

-------------------
-- PLUGINS SETUP --
-------------------
require("lazy").setup({
  spec = {
    ----------------
    -- TOKYONIGHT --
    ----------------
    {
      "folke/tokyonight.nvim",
      lazy = false,
      priority = 1000,
      config = function()
        vim.cmd([[colorscheme tokyonight-night]])
      end,
    },

    --------------
    -- NEO-TREE --
    --------------
    {
      "nvim-neo-tree/neo-tree.nvim",
      branch = "v3.x",
      dependencies = {
        "nvim-lua/plenary.nvim",
        "nvim-tree/nvim-web-devicons",
        "MunifTanjim/nui.nvim"
      },
      opts = {
        close_if_last_window = true,
        default_component_configs = {
          indent = {
            with_expanders = true,
            expander_collapsed = '',
            expander_expanded = ''
          }
        }
      }
    },

    -----------
    -- NOICE --
    -----------
    {
      "folke/noice.nvim",
      event = "VeryLazy",
      opts = {
        cmdline = {
          format = {
            search_down = { view = "cmdline" },
            search_up = { view = "cmdline" }
          }
        },
      },
      dependencies = {
        "MunifTanjim/nui.nvim",
        "rcarriga/nvim-notify"
      }
    },
    -- C'est un peu dans noice quand même
    {
      "rcarriga/nvim-notify",
      opts = {
        render = "simple",
        stages = "fade_in_slide_out",
        timeout = 600,
        top_down = false,
      }
    },

    ---------------
    -- WHICH-KEY --
    ---------------
    {
      "folke/which-key.nvim",
      event = "VeryLazy",
      opts = {
        preset = "modern",
        delay = 1000
      },
      keys = {
        {
          "<leader>?",
          function()
            require("which-key").show({ global = false })
          end,
          desc = "Buffer Local Keymaps (which-key)",
        }
      }
    },

    ----------------
    -- TREESITTER --
    ----------------
    {
      'nvim-treesitter/nvim-treesitter',
      build = ":TSUpdate",
      config = function ()
        local configs = require("nvim-treesitter.configs")
        configs.setup({
          ensure_installed = { "lua", "vim", "vimdoc", "hyprlang", "rust", "python", "toml", "bash", "fish", "markdown", "ocaml", "regex", "rasi"},
          sync_install = false,
          highlight = { enable = true },
          indent = { enable = true },
        })
      end
    },

    {
      "lukas-reineke/indent-blankline.nvim",
      main = "ibl",
      opts = {
        viewport_buffer = {
          min = 50
        },
        scope = {
          enabled = false,
          show_start = false,
          show_end = false
        }
      },
    },

    { 'neovim/nvim-lspconfig', version = "*" },
    { 'hrsh7th/nvim-cmp', version = "*" },
    { 'hrsh7th/cmp-buffer', version = "*" },
    { 'hrsh7th/cmp-path', version = "*" },
    { 'hrsh7th/cmp-nvim-lsp', version = "*" },
    { 'norcalli/nvim-colorizer.lua', version = "*" },
    { 'echasnovski/mini.ai', version = "*" },
    { 'echasnovski/mini.icons', version = "*" },
    { 'echasnovski/mini.indentscope', version = '*' },
    { 'echasnovski/mini.pairs', version = "*" },
    { 'echasnovski/mini.bufremove', version = "*" },
    { "folke/todo-comments.nvim", dependencies = { "nvim-lua/plenary.nvim" }, },
    { 'akinsho/bufferline.nvim', version = "*", dependencies = 'nvim-tree/nvim-web-devicons' },
    { 'nvim-lualine/lualine.nvim', dependencies = 'nvim-tree/nvim-web-devicons' },
  },

  install = { colorscheme = { "tokyonight" } },

  checker = { enabled = true },
})

require("todo-comments").setup()
require('mini.pairs').setup()
require('mini.ai').setup()
require('mini.indentscope').setup({ symbol = "▏" })
require('colorizer').setup()

----------------
-- BUFFERLINE --
----------------
require('bufferline').setup {
  options = {
    mode = "buffers",
    separator_style = "slant",
    always_show_bufferline = true,
    hover = {
      enabled = true,
      delay = 200,
      reveal = {"close"}
    }
  }
}

-------------
-- LUALINE --
-------------
require('lualine').setup {
  options = {
    icons_enabled = true,
    theme = 'auto',
    component_separators = { left = '', right = ''},
    section_separators = { left = '', right = ''},
    ignore_focus = {},
    always_divide_middle = true,
    always_show_tabline = true,
    globalstatus = true,
    refresh = {
      statusline = 100,
      tabline = 100,
      winbar = 100,
    }
  },
  sections = {
    lualine_a = {'mode'},
    lualine_b = {'branch', 'diff', 'diagnostics'},
    lualine_c = {{'filename', symbols = {modified = " ", readonly = " ", unnamed = " ", newfile = " "}}},
    lualine_x = {'encoding', 'fileformat', 'filetype'},
    lualine_y = {'progress'},
    lualine_z = {'location'}
  },
  inactive_sections = {
    lualine_a = {},
    lualine_b = {},
    lualine_c = {'filename'},
    lualine_x = {'location'},
    lualine_y = {},
    lualine_z = {}
  }
}


-----------
-- NOICE --
-----------
require("noice").setup({
  views = {
    cmdline_popup = {
      position = { row = 5, col = "50%" },
      size = { width = 60, height = "auto" },
    },
    popupmenu = {
      relative = "editor",
      position = { row = 8, col = "50%" },
      size = { width = 60, height = 10 },
      border = { style = "rounded", padding = { 0, 1 } },
      win_options = {
        winhighlight = { Normal = "Normal", FloatBorder = "DiagnosticInfo" }
      }
    }
  },
  routes = {
    {
      filter = {
        event = "msg_show",
        kind = "",
        find = "written",
      },
      opts = { skip = true },
    },
    {
      filter = {
        event = "msg_show",
        kind = "",
        find = "fewer",
      },
      opts = { skip = true },
    }
  }
})

-------------
-- KEYMAPS --
-------------
-- Oublie pas que tu peux faire K pour avoir l'help du LSP quand tu hover un truc
-- <C-]> pour jump à la def
vim.keymap.set('n', '<leader>e', function()
  local reveal_file = vim.fn.expand('%:p')
  if (reveal_file == '') then
    reveal_file = vim.fn.getcwd()
  else
    local f = io.open(reveal_file, "r")
    if (f) then
      f.close(f)
    else
      reveal_file = vim.fn.getcwd()
    end
  end
  require('neo-tree.command').execute({
    action = "focus",
    source = "filesystem",
    position = "left",
    toggle = true,
    reveal_file = reveal_file,
    reveal_force_cwd = true,
  })
  end,
  { desc = "Open neo-tree at current file or working directory" }
);

vim.keymap.set('t', '<Esc>', '<C-\\><C-n>', { noremap = true, silent = true})

-- Tellement pratique. La base
-- Si besoin tu peux le faire pour plein d'autres commandes
vim.keymap.set('n', 'u', ':silent undo<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<C-R>', ':silent redo<CR>', { noremap = true, silent = true })
vim.keymap.set("i", ",,", "<Esc>")
vim.keymap.set("n", "<Esc>", ":noh<CR>", { noremap = true, silent = true })

-- Pour changer de window
vim.keymap.set({ "n", "v", "i" }, "<C-h>", "<C-w>h")
vim.keymap.set({ "n", "v", "i" }, "<C-j>", "<C-w>j")
vim.keymap.set({ "n", "v", "i" }, "<C-k>", "<C-w>k")
vim.keymap.set({ "n", "v", "i" }, "<C-l>", "<C-w>l")

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
wk.add({
  { "<leader>v", group = "splits" },
  { "<leader>vd", "<cmd>q<CR>", desc = "Delete window" },
  { "<leader>vh", "<cmd>vsplit<CR><C-w>h", desc = "Right-side not focused window" },
  { "<leader>vj", "<cmd>split<CR>", desc = "Bottom focused window" },
  { "<leader>vk", "<cmd>split<CR><C-w>k", desc = "Bottom not focused window" },
  { "<leader>vl", "<cmd>vsplit<CR>", desc = "Right-side focused window" },
})

---------
-- LSP --
---------

vim.lsp.enable('qmlls')

vim.lsp.config('qmlls', {
    cmd = {"qmlls6", "-E"}
})

vim.lsp.enable('pyright')

vim.lsp.config('pyright', {
  settings = {
    python = {
      analysis = {
        logLevel = "Warning"
      }
    }
  }
})

vim.lsp.config('rust_analyzer', {
  on_attach = function(client, bufnr)
    vim.lsp.inlay_hint.enable(true, { bufnr = bufnr })
  end,
  settings = {
    ["rust-analyzer"] = {
      imports = {
        granularity = { group = "module" },
        prefix = "self"
      },
      cargo = {
        buildScripts = { enable = true },
      },
      procMacro = { enable = true }
    }
  }
})

----------------
-- Completion --
----------------
local cmp = require('cmp')

-- On ne complète pas dans les commentaires !!!
cmp.setup{
  enabled = function()
    local context = require 'cmp.config.context'
    if vim.api.nvim_get_mode().mode == 'c' then
      return true
    else
      -- On enlève aussi la completion dans les strings parce que ça casse les couilles
      return not (context.in_treesitter_capture("comment")
        or context.in_syntax_group("Comment") or (context.in_treesitter_capture("string") and not context.in_treesitter_capture("string.special.path")))
    end
  end,
  -- Jsp si c'est vraiment nécessaire tout ça
  matching = {
    disallow_fuzzy_matching = false,
    disallow_fullfuzzy_matching = false,
    disallow_partial_matching = false,
    disallow_partial_fuzzy_matching = false,
    disallow_prefix_unmatching = false,
  },
  experimental = {
    ghost_text = true
  },
  mapping = cmp.mapping.preset.insert({
    ['<C-p>'] = cmp.mapping.select_prev_item(),
    ['<C-n>'] = cmp.mapping.select_next_item(),
    ['<C-b>'] = cmp.mapping.scroll_docs(-4),
    ['<C-f>'] = cmp.mapping.scroll_docs(4),
    ['<C-Space>'] = cmp.mapping.complete(),
    ['<Tab>'] = cmp.mapping.confirm({ select = true })
  }),
  sources = cmp.config.sources({
    { name = 'nvim_lsp', keyword_length = 2 },
    { name = 'buffer' },
    { name = 'path' },
  })
}

-- On enlève les ptns de message de pylsp qui dit "linting jsp" toutes les 5 secondes
vim.lsp.handlers['$/progress'] = function(_, result, ctx)
  local value = result.value
  if not value.kind then
      return
  end
  local client_id = ctx.client_id
  local name = vim.lsp.get_client_by_id(client_id).name
  if name == 'pylsp' then
    return
  end
  vim.notify(value.message, 'info', {
      title = value.title,
  })
end

local capabilities = require('cmp_nvim_lsp').default_capabilities()
