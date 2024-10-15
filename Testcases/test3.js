const fetch = require('node-fetch');

it('should enforce CORS policies', async function () {
    // Attempt to access the API from an unauthorized origin
    const response = await fetch('http://localhost:3000/contact', {
        method: 'POST',
        headers: {
            'Origin': 'http://unauthorized-origin.com',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: 'Test',
            email: 'test@example.com',
            message: 'Test message.'
        })
    });

    // Assert that the response status is not 200
    expect(response.status).to.not.equal(200);
});
