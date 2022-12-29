#!/usr/bin/node

// creating an object
let user = {
    name: 'me', //key: value pair
    age: 30,
    email: 'me@me.com',
    location: 'just',
    blogs: ['but why', 'mehn'],
    login() {//methods: things the object can do
        console.log('user is logged in');
    },
    logout() {
        console.log('user logged out');
    },

    logBlogs() {
    this.blogs.forEach(blog => {
        console.log(blog);
        })
    }
};

//object.method name()


let b = 1;
function myFunction(a) {
    console.log(a + b);
    b = a;
}

myFunction(3);
myFunction(4);



