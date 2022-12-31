import { defineConfig } from 'vitepress'
import { META_TITLE, META_DESCRIPTION, head } from './configs/head'
import { nav } from './configs/nav'
import { sidebar } from './configs/sidebar'

export default defineConfig({
  lang: 'en-US',
  title: META_TITLE,
  description: META_DESCRIPTION,

  head,

  themeConfig: {
    logo: '/logo.svg',

    editLink: {
      pattern: 'https://github.com/n6ai/n6py/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },

    socialLinks: [{ icon: 'github', link: 'https://github.com/n6ai/n6py' }],

    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2022-present Sergej Samsonenko'
    },

    nav,
    sidebar
  }
})
