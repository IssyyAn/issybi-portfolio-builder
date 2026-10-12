import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const html=fs.readFileSync(new URL('../examples/dashboard-mockup.html',import.meta.url),'utf8');
const script=html.match(/<script>([\s\S]*?)<\/script>/)[1];
const elements=new Map();
function element(id){if(!elements.has(id)){const el={value:id==='region'?'All regions':id==='category'?'All categories':'',textContent:'',innerHTML:'',handlers:{},addEventListener(event,fn){this.handlers[event]=fn;}};Object.defineProperty(el,'selectedIndex',{set(index){assert.equal(index,0);this.value=id==='region'?'All regions':'All categories';}});elements.set(id,el);}return elements.get(id);}
const context=vm.createContext({document:{getElementById:element},Intl});
vm.runInContext(script,context);
function verify(region,category,total,count){element('region').value=region;element('category').value=category;element('region').handlers.change();assert.equal(element('total').textContent,total);assert.equal(element('count').textContent,count);const rows=(element('details').innerHTML.match(/<tr>/g)||[]).length;assert.equal(rows,count?count+1:0);if(!count){for(const id of ['trend','breakdown','details'])assert.match(element(id).innerHTML,/No matching records/);assert.equal(element('leader').textContent,'—');}}
verify('All regions','All categories','$476,400',30);
verify('North','All categories','$271,800',18);
verify('All regions','Furniture','$78,000',6);
verify('North','Technology','$90,600',6);
verify('South','Furniture','$0',0);
element('reset').handlers.click();assert.equal(element('region').value,'All regions');assert.equal(element('category').value,'All categories');assert.equal(element('total').textContent,'$476,400');assert.equal(element('count').textContent,30);
assert.match(html,/Illustrative \/ synthetic data — not real findings/);
assert.doesNotMatch(html,/<script[^>]*src=|<link[^>]*href=["']https?:/i);
console.log('PASS: initial, region, category, combined, empty and reset states; known aggregate/row counts; synthetic label; no external script/style dependencies. DOM stub only: browser rendering, native controls and accessibility remain unverified.');
