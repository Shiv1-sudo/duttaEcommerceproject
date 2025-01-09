document.addEventListener('DOMContentLoaded', function() {
    try {
        var formElement = document.getElementById('login-form');
        console.log('Form element:', formElement);

        var otpSent = formElement.getAttribute('data-otp-sent');
        console.log('OTP sent attribute:', otpSent);

        if (otpSent === 'true') {
            console.log('OTP sent is true, showing OTP section.');
            document.getElementById('otp-section').style.display = 'block';
            document.getElementById('send-otp-button').disabled = true;
            document.getElementById('password-field').disabled = true;
            document.getElementById('email-field').disabled = true;
        }
    } catch (error) {
        console.error('Error during DOMContentLoaded event:', error);
    }
});

function handleSendOTP(event) {
    try {
        event.preventDefault();
        var sendOtpButton = document.getElementById('send-otp-button');
        console.log('Send OTP button:', sendOtpButton);

        sendOtpButton.disabled = true;
        console.log('Disabling send OTP button.');

        document.getElementById('otp-section').style.display = 'block';
        console.log('Showing OTP section.');

        document.getElementById('password-field').disabled = true;
        document.getElementById('email-field').disabled = true;

        console.log('Disabling email and password fields.');

        document.getElementById('login-form').submit();
        console.log('Form submitted.');
    } catch (error) {
        console.error('Error during handleSendOTP function:', error);
    }
}
