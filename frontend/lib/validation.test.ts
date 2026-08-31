import {describe,it,expect} from 'vitest'; import {validateSources} from './validation';
describe('source validation',()=>{it('accepts bounded public https sources',()=>expect(validateSources(['https://example.com/docs'])).toBe(true));it('rejects unsafe or unbounded sets',()=>{expect(validateSources([])).toBe(false);expect(validateSources(['http://example.com'])).toBe(false);expect(validateSources(['https://localhost/x'])).toBe(false);expect(validateSources(['https://a.com','https://b.com','https://c.com','https://d.com'])).toBe(false)})})
describe('source boundary matrix',()=>{
  const accepted=['https://docs.example.com/a?x=1','https://genlayer.org','https://example.com:443/path','https://a-b.example.co.uk'];
  const rejected=['ftp://example.com','javascript:alert(1)','https://127.0.0.1','https://0.0.0.0','https://192.168.1.1','https://10.0.0.1','https://172.16.0.1','https://169.254.1.1','https://224.0.0.1','https://255.255.255.255','https://[::1]','https://user@example.com','https://user:pass@example.com','https://x.local','not a url','https://'];
  accepted.forEach((value)=>it(`accepts ${value}`,()=>expect(validateSources([value])).toBe(true)));
  rejected.forEach((value)=>it(`rejects ${value}`,()=>expect(validateSources([value])).toBe(false)));
  it('allows one to three sources',()=>{expect(validateSources(['https://a.example','https://b.example','https://c.example'])).toBe(true);});
  it('rejects four sources',()=>expect(validateSources(['https://a.example','https://b.example','https://c.example','https://d.example'])).toBe(false));
});
