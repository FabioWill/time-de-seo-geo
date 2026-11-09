/**
 * commitlint.config.cjs
 *
 * Purpose: enforces Conventional Commits with a mandatory scope (see CONTRIBUTING.md).
 * Exports: commitlint config object.
 * Shared:  .husky/commit-msg runs it on every commit.
 */
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'scope-empty': [2, 'never'],
    'scope-enum': [2, 'always', ['regua', 'conferir', 'preparar', 'guia', 'casos', 'pesquisa', 'agentes', 'exemplo', 'repo']],
  },
};
