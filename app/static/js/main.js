/**
 * main.js - Iko's Restaurant
 * Système complet d'authentification et interface
 */

document.addEventListener('DOMContentLoaded', function() {
    
    // =========================================================
    // 1. NAVBAR : Effet au scroll
    // =========================================================
    const nav = document.querySelector('.navbar-ikos');
    if (nav) {
        window.addEventListener('scroll', () => {
            nav.classList.toggle('navbar-scrolled', window.scrollY > 50);
        });
    }

    // =========================================================
    // 2. TOGGLE PASSWORD (Afficher/Masquer)
    // =========================================================
    document.querySelectorAll('.password-toggle').forEach(toggle => {
        toggle.addEventListener('click', function() {
            const input = this.parentElement.querySelector('input');
            if (!input) return;

            const isHidden = input.type === 'password';
            input.type = isHidden ? 'text' : 'password';
            
            // Switch d'icône via les data-attributes
            this.src = isHidden ? this.dataset.hidePath : this.dataset.showPath;
            this.alt = isHidden ? "Masquer" : "Afficher";
        });
    });

    // =========================================================
    // 3. VALIDATION COMPLÈTE (Inscription)
    // =========================================================
    const regInput = document.getElementById('regPassword');
    const regEmail = document.getElementById('regEmail');
    const emailFeedback = document.getElementById('email-feedback');
    const submitBtn = document.querySelector('#section-register button[type="submit"]');

    if (regInput && regEmail) {
        
        // --- Validation du Mot de Passe ---
        function validatePassword(forceErrors = false) {
            const val = regInput.value;
            const isEmpty = val.length === 0;
            const firstIcon = document.querySelector('.req-icon');
            
            const rules = {
                'req-length': val.length >= 10,
                'req-cases': /[a-z]/.test(val) && /[A-Z]/.test(val),
                'req-numbers': /[0-9]/.test(val),
                'req-special': /[!?#%$*]/.test(val)
            };

            let allPwdValid = true;

            Object.entries(rules).forEach(([id, isMet]) => {
                const container = document.getElementById(id);
                if (!container) return;
                const icon = container.querySelector('.req-icon');
                if (!isMet) allPwdValid = false;

                if (isMet) {
                    container.className = 'text-success fw-bold d-flex align-items-center mb-1';
                    icon.src = firstIcon.dataset.green;
                } else if (isEmpty) {
                    container.className = 'text-muted d-flex align-items-center mb-1';
                    icon.src = firstIcon.dataset.gray;
                } else if (forceErrors) {
                    container.className = 'text-danger d-flex align-items-center mb-1';
                    icon.src = firstIcon.dataset.red;
                } else {
                    container.className = 'text-muted d-flex align-items-center mb-1';
                    icon.src = firstIcon.dataset.gray;
                }
            });
            return allPwdValid;
        }

        // --- Validation de l'Email ---
        function validateEmail(forceError = false) {
            const emailValue = regEmail.value;
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            const isValid = emailRegex.test(emailValue);

            if (emailValue.length === 0) {
                emailFeedback.style.display = 'none';
                regEmail.classList.remove('is-invalid');
            } else if (isValid) {
                emailFeedback.style.display = 'none';
                regEmail.classList.remove('is-invalid');
                regEmail.classList.add('is-valid');
            } else if (forceError) {
                emailFeedback.style.display = 'block';
                regEmail.classList.add('is-invalid');
            }
            return isValid;
        }

        // --- Mise à jour de l'état du bouton ---
        function updateSubmitButton() {
            const isEmailOk = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(regEmail.value);
            const val = regInput.value;
            const isPwdOk = (val.length >= 10 && /[a-z]/.test(val) && /[A-Z]/.test(val) && /[0-9]/.test(val) && /[!?#%$*]/.test(val));
            
            submitBtn.disabled = !(isEmailOk && isPwdOk);
            submitBtn.style.opacity = submitBtn.disabled ? "0.5" : "1";
        }

        // Événements Email
        regEmail.addEventListener('input', () => { validateEmail(false); updateSubmitButton(); });
        regEmail.addEventListener('blur', () => validateEmail(true));

        // Événements Password
        regInput.addEventListener('input', () => { validatePassword(false); updateSubmitButton(); });
        regInput.addEventListener('blur', () => validatePassword(true));

        // Initialisation du bouton
        updateSubmitButton();
    }

    // =========================================================
    // 4. SIDEBAR AUTH : Reset à la fermeture
    // =========================================================
    const sidebarAuth = document.getElementById('sidebarAuth');
    if (sidebarAuth) {
        sidebarAuth.addEventListener('hidden.bs.offcanvas', () => switchAuth('login'));
    }

    console.log("✅ Système Iko's Restaurant opérationnel.");
});

/**
 * Fonction globale pour switcher les vues
 */
function switchAuth(view) {
    const loginView = document.getElementById('section-login');
    const registerView = document.getElementById('section-register');
    if (loginView && registerView) {
        const isReg = view === 'register';
        loginView.style.display = isReg ? 'none' : 'block';
        registerView.style.display = isReg ? 'block' : 'none';
    }
}