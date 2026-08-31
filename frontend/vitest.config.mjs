/** @type {import('vitest/config').UserConfig} */
export default { root: new URL('.', import.meta.url).pathname, test: { environment: 'jsdom', include: ['lib/**/*.test.ts'] } };
