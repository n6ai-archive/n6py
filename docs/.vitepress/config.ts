import { defineConfig } from 'vitepress'
import sidebar from './sidebar'

export default defineConfig({
  lang: 'en-US',
  title: 'n6py',
  description:
    'Python Power Tools for Scientific Computing, Machine Learning and Deep Learning.',

  head: [['link', { rel: 'icon', type: 'image/svg+xml', href: '/logo.svg' }]],

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

    nav: [
      { text: 'Guide', link: '/guide/' },
      { text: 'API', link: '/api/' }
    ],

    sidebar
  }
})
