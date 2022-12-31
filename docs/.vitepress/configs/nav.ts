import { useVersion } from '../composables/use-version'

const version = await useVersion()

export const nav = [
  { text: 'Guide', link: '/guide/' },
  { text: 'API', link: '/api/' },
  {
    text: version,
    items: [
      {
        text: 'PyPI Package',
        link: 'https://pypi.org/project/n6py/'
      },
      {
        text: 'Changelog',
        link: 'https://github.com/n6ai/n6py/blob/main/CHANGELOG.md'
      },
      {
        text: 'Contributing',
        link: 'https://github.com/n6ai/n6py/blob/main/.github/CONTRIBUTING.md'
      }
    ]
  }
]
