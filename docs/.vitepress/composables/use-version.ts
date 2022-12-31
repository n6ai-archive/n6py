import { resolve, dirname } from 'node:path'
import { fileURLToPath } from 'url'
import fs from 'node:fs/promises'

export async function useVersion() {
  const __filename = fileURLToPath(import.meta.url)
  const __dirname = dirname(__filename)

  const file = resolve(__dirname, '../../../pyproject.toml')
  const data = await fs.readFile(file, 'utf-8')
  const version = data.match(/(?!version\s*=\s*"?)\d+\.\d+\.\d+.*(?=")/gim)?.[0]
  return version
}
