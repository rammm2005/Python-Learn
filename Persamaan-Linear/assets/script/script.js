function generateInputs() {
    const n = document.getElementById('variables').value;
    const matrixInputs = document.getElementById('matrix-inputs');
    const vectorInput = document.getElementById('vector-input');

    matrixInputs.innerHTML = '';
    vectorInput.innerHTML = '';

    for (let i = 0; i < n; i++) {
        let rowInput = document.createElement('input');
        rowInput.type = 'text';
        rowInput.name = `row${i + 1}`;
        rowInput.placeholder = `Enter row ${i + 1} elements separated by space`;
        rowInput.required = true;
        matrixInputs.appendChild(rowInput);
        matrixInputs.appendChild(document.createElement('br'));
    }

    let bInput = document.createElement('input');
    bInput.type = 'text';
    bInput.name = 'vector';
    bInput.placeholder = 'Enter vector elements separated by space';
    bInput.required = true;
    vectorInput.appendChild(bInput);
}
