import type { HeadConfig } from 'vitepress'

export const META_URL = 'https://py.n6.ai'
export const META_TITLE = 'n6py'
export const META_DESCRIPTION =
  'Python Power Tools for Scientific Computing, Machine Learning and Deep Learning.'
export const META_IMAGE = 'https://py.n6.ai/social.jpg'

export const head: HeadConfig[] = [
  ['link', { rel: 'icon', type: 'image/svg+xml', href: '/logo.svg' }],
  ['link', { rel: 'icon', type: 'image/png', href: '/logo.png' }],
  ['meta', { property: 'og:type', content: 'website' }],
  ['meta', { property: 'og:url', content: META_URL }],
  ['meta', { property: 'og:title', content: META_TITLE }],
  ['meta', { property: 'og:description', content: META_DESCRIPTION }],
  ['meta', { property: 'og:image', content: META_IMAGE }],
  ['meta', { property: 'og:image:alt', content: 'Preview of n6py' }],
  ['meta', { property: 'twitter:card', content: 'summary_large_image' }],
  ['meta', { property: 'twitter:url', content: META_URL }],
  ['meta', { property: 'twitter:title', content: META_TITLE }],
  ['meta', { property: 'twitter:description', content: META_DESCRIPTION }],
  ['meta', { property: 'twitter:image', content: META_IMAGE }]
]
