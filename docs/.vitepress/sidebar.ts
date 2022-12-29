import type { DefaultTheme } from 'vitepress'

export const sidebar: DefaultTheme.Sidebar = {
  '/guide/': [
    {
      text: 'Guide',
      items: [
        {
          text: 'Quick Start',
          link: '/guide/'
        },
        {
          text: 'About',
          link: '/guide/about'
        }
      ]
    }
  ],
  '/api/': [
    {
      text: 'API',
      items: [
        {
          text: 'display',
          link: '/api/display'
        },
        {
          text: 'encode',
          link: '/api/encode'
        },
        {
          text: 'stats',
          link: '/api/stats'
        }
      ]
    }
  ]
}
