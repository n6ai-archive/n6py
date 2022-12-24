import type { DefaultTheme } from 'vitepress'

const sidebar: DefaultTheme.Sidebar = {
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

export default sidebar
