const row = '.col\n';
const base = '  button.btn.btn-primary#';
let id = 0;
const buildRow = (num) => {
    let s = row;
    for (let i = 1; i <= num; ++i) {
        s += base + id + '\n';
        ++id;
    }
    return s;
};

for (let i = 0; i != 3; ++i)
    console.log(buildRow(10));

