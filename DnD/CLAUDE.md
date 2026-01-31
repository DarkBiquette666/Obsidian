# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an Obsidian vault for managing Dungeons & Dragons content. It is not a code repository but a knowledge base using Markdown files.

## Plugin Development

When working on the D&D Content Plugin located at `D:\Git\Obsidian Plugins\obsidian-dnd-content`:
- ALWAYS refer to the README.md in the plugin directory for architecture and design decisions
- ALWAYS update the README.md when making significant changes to the plugin
- The plugin follows a data-driven architecture: data is in the vault, not in the code
- See README.md for complete documentation on parsers, data formats, and component structure

## Vault Structure

- **Campagne/** - Main Campaign Content and Story Engine.
- **Glossary/** - The Database (Rules, Bestiary, Spells, Items, etc.).
- **Dons/** - Feats Database ONLY (Do not use for Campaign Content).
- **Resources/** - Reference materials, rules, and shared resources
- **.obsidian/** - Obsidian configuration (do not modify manually)

## Working with this Vault

When creating or editing content:
- Use standard Markdown with Obsidian-flavored extensions
- Use `[[wikilinks]]` for internal links between notes
- Use `#tags` for categorization
- Use YAML frontmatter for metadata properties
- Never use Emojis
- Never sign commits with the Anthropic signature

## Enabled Obsidian Features

The vault uses: daily notes, templates, graph view, backlinks, canvas, bookmarks, and Obsidian Sync.
