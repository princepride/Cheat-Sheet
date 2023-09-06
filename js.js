//在js中this在function和箭头中是不一样的
let a1={b:1,c:2,d:this,e:()=>{return this}}
console.log(a1.d)//Window {window: Window, self: Window, document: document, name: '', location: Location, …}
console.log(a1.e())//Window {window: Window, self: Window, document: document, name: '', location: Location, …}

let a2={b:1,c:2,d:this,e:function(){return this}}
console.log(a2.e())//{b: 1, c: 2, d: Window, e: ƒ}

//可以像这样插入子元素

const START1 = `<svg
        xmlns="http://www.w3.org/2000/svg"
        class="star-icon"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        stroke-width="2">
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
      </svg>`

      let newDiv = document.createElement('div');
      newDiv.innerHTML = START1;
      document.querySelector('body').appendChild(newDiv);
