const stripePublicKey = document.querySelector('#stripe-public-key').innerText.slice(1, -1);
const clientSecret = document.querySelector('#client-secret').innerText.slice(1, -1);

const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

const style = {
    base: {
        color: '#000',
        fontFamily: '"Roboto", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '1.2rem',
        fontWeight: 'normal',
        '::placeholder': {
            color: '#aab7c4'
        },
        backgroundColor: '#ffffff',
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

const card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', e => {
    const errorDiv = document.getElementById('card-errors');
    if (e.error) {
        let html  = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${e.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

const form = document.getElementById('payment-form');

form.addEventListener('submit', ev => {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(result => {
        if (result.error) {
            const errorDiv = document.getElementById('card-errors');
            let html  = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false });
            $('#submit-button').attr('disabled', false);

        } else {
          if (result.paymentIntent.status === 'succeeded') {
              form.submit();
          }  
        }
    });
});