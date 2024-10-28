return {
  {
    "neovim/nvim-lspconfig",
    opts = {
      document_highlight = { enabled = false },
      servers = {
        ruff_lsp = {
          mason = false,
          autostart = false,
        },
        ruff = {
          mason = false,
          autostart = false,
        },
        pyright = {
          settings = {
            python = {
              analysis = {
                typeCheckingMode = "off",
                autoImportCompletions = true,
              },
            },
          },
        },
      },
    },
  },
}
