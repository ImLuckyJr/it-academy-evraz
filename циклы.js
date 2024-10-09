let a = {
    'ab': '123',
    'ba': '234',
    'aaa': '456',
};

// for (let i of a) {
//     console.log(i);
// }

for (let i in a) {
    console.log(i, a[i]);
}

// for (let i = 0; i < a.length; i++) { // ++i
//     console.log(i, a[i]);
// }
