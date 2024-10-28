return {
  {
    "hrsh7th/nvim-cmp",
    init = function()
      vim.g.cmp_disabled = false
    end,
    opts = function(_, opts)
      opts.enabled = function()
        -- local context = require("cmp.config.context")
        if vim.g.cmp_disabled == true then
          return false
        end
        -- some other conditions (like not in commments) can go here
        local context = require 'cmp.config.context'
        return not context.in_treesitter_capture("comment") and not context.in_syntax_group("Comment")
      end
    end,
  },
}
