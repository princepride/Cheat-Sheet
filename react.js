//The usage of useRef()
//useRef is a React Hook that returns a mutable object with a single property current. 
//The current property is initialized to the value passed as the argument to useRef, 
//and its value can be updated throughout the lifetime of a component.
//Here's an example of using useRef to access the DOM element in a component:
//In this example, useRef is used to create a reference inputRef to the input element. 
//The useEffect hook is used to focus the input element when the component is rendered. 
//The second argument to useEffect is an empty array, which means the effect will only run once, 
//when the component is mounted. The ref callback function is passed the actual DOM node of the input element and sets the inputRef.
//current property to that node. Finally, the inputRef.current property is used in the useEffect hook to access the input element and call its focus method.
//This program's result is that the input element will be focused when the component is rendered.
const MyComponent = () => {
    const inputRef = useRef(null);
  
    useEffect(() => {
      inputRef.current.focus();
    }, []);
  
    return <input type="text" ref={inputRef} />;
  };


//The usage of useCallback()
const wrapperRef = useCallback(wrapper => {
    if (wrapper == null) return
    wrapper.innerHTML = ""
    const editor = document.createElement("div")
    wrapper.append(editor)
    new Quill(editor, {theme:"snow"})
},[]); 

<div id="container" ref={wrapperRef}></div>
//The code you provided creates a div element with an id of container and a ref callback function wrapperRef.

//When the component that contains this div is rendered, the ref function wrapperRef will be passed the actual DOM node of the div element with an id of container.

//This means that you'll be able to access the div element through wrapperRef and perform any necessary operations on it. In this case, the wrapperRef function creates a rich text editor using the Quill library and appends it to the div element specified by the ref.

//So, if you run this code, the result would be that a rich text editor will be created inside the div with id equal to container.