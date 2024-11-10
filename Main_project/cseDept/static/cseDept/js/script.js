const { jsPDF } = window.jspdf;

function showInputSection() {
    const budget = document.getElementById('budget').value;
    const inputSection = document.getElementById('inputSection');
    const additionalInputs = document.getElementById('additionalInputs');

    additionalInputs.innerHTML = '';

    if (budget < 50000) {
        additionalInputs.innerHTML = `
            <label for="item">Item:</label>
            <input type="text" id="item" name="item" required><br><br>
            <label for="purpose">Purpose:</label>
            <input type="text" id="purpose" name="purpose" required><br><br>
            <label for="cost">Cost (Rs):</label>
            <input type="number" id="cost" name="cost" required><br><br>
            <label for="vendor">Vendor:</label>
            <input type="text" id="vendor" name="vendor" required><br><br>
            <label for="person">Person Responsible:</label>
            <input type="text" id="person" name="person" required><br><br>
            <label for="comments">Comments:</label>
            <textarea id="comments" name="comments" required></textarea><br><br>
        `;
    } else {
        additionalInputs.innerHTML = `
            <label for="product">Product:</label>
            <input type="text" id="product" name="product" required><br><br>
            <label for="vendor">Vendor:</label>
            <input type="text" id="vendor" name="vendor" required><br><br>
            <label for="amount">Amount (Rs):</label>
            <input type="number" id="amount" name="amount" required><br><br>
            <label for="date">Date:</label>
            <input type="date" id="date" name="date" required><br><br>
        `;
    }

    inputSection.style.display = 'block';
}

function generateLetter() {
    const budget = document.getElementById('budget').value;
    const contentDiv = document.getElementById('content');
    const responsiblePerson = document.getElementById('responsible-person');
    const date = new Date().toLocaleDateString('en-GB');

    if (budget < 50000) {
        const item = document.getElementById('item').value;
        const purpose = document.getElementById('purpose').value;
        const cost = document.getElementById('cost').value;
        const vendor = document.getElementById('vendor').value;
        const person = document.getElementById('person').value;
        const comments = document.getElementById('comments').value;

        contentDiv.innerHTML = `
            <p>To,<br>
            The Registrar,<br>
            K.L.E. Technological University,<br>
            Hubli</p>
            <p>Sir,</p>
            <p><strong>Subject: Request to procure consumables for Machines and Mechanisms Lab.</strong></p>
            <p>Item: ${item}<br>
            Purpose: ${purpose}<br>
            Cost: Rs.${cost}/- including taxes<br>
            Company / Supplier: ${vendor}<br>
            Person Responsible at SME: ${person}</p>
            <p>Comments: ${comments}</p>
            <p>Date: ${date}</p>
        `;
        responsiblePerson.textContent = person;
    } else {
        const product = document.getElementById('product').value;
        const vendor = document.getElementById('vendor').value;
        const amount = document.getElementById('amount').value;
        const inputDate = document.getElementById('date').value;
        const formattedDate = new Date(inputDate).toLocaleDateString('en-GB');

        contentDiv.innerHTML = `
            <p>Date: ${formattedDate}</p>
            <p>To,<br>
            The Registrar,<br>
            KLE Technological University,<br>
            BVB Campus,<br>
            Hubballi</p>
            <p>From,<br>
            The Head,<br>
            School of Mechanical Engineering,<br>
            KLE Technological University,<br>
            BVB Campus,<br>
            Hubballi</p>
            <p>Sir,</p>
            <p><strong>Subject: Permission to purchase ${product} reg.</strong></p>
            <p>We need ${product} for CARR laboratory. The product has proprietary hardware and software and it can be procured directly from the vendor. We have received the quotation from the vendor on ${formattedDate}. The approximate cost is around Rs.${amount}/-. I request your kind approval of the purchase and necessary sanction for the same.</p>
            <p>Thanking you,</p>
            <p>Yours faithfully,</p>
            <p>Encl:<br>1. Quotation</p>
        `;
        responsiblePerson.textContent = 'The Head, School of Mechanical Engineering';
    }

    document.getElementById('letter').style.display = 'block';
    document.getElementById('downloadPdf').style.display = 'block';
    document.getElementById('sendApproval').style.display = 'block';
}

function downloadPDF() {
    const letter = document.getElementById('letter');
    const pdf = new jsPDF();

    html2canvas(letter).then(canvas => {
        const imgData = canvas.toDataURL('image/png');
        pdf.addImage(imgData, 'PNG', 10, 10);
        pdf.save('procurement_request.pdf');
    });
}

function sendForApproval() {
    const formData = new FormData(document.getElementById('procurementForm'));
    fetch('/submit', {
        method: 'POST',
        body: formData
    }).then(response => {
        if (response.ok) {
            alert('Request sent for approval.');
        } else {
            alert('Failed to send the request.');
        }
    }).catch(error => {
        console.error('Error:', error);
        alert('Failed to send the request.');
    });
}
