# file lib/ansible/plugins/become/su.py:94-135
# lines [94, 96, 99, 101]
# branches []

import pytest
from ansible.plugins.become import su

def test_su_prompt_localizations():
    # Create an instance of the BecomeModule class
    become_module = su.BecomeModule()
    
    # Check that the name attribute is correctly set
    assert become_module.name == 'su'
    
    # Check that the fail attribute is correctly set
    assert become_module.fail == ('Authentication failure',)
    
    # Check that the SU_PROMPT_LOCALIZATIONS list is correctly set
    expected_localizations = [
        'Password',
        '암호',
        'パスワード',
        'Adgangskode',
        'Contraseña',
        'Contrasenya',
        'Hasło',
        'Heslo',
        'Jelszó',
        'Lösenord',
        'Mật khẩu',
        'Mot de passe',
        'Parola',
        'Parool',
        'Pasahitza',
        'Passord',
        'Passwort',
        'Salasana',
        'Sandi',
        'Senha',
        'Wachtwoord',
        'ססמה',
        'Лозинка',
        'Парола',
        'Пароль',
        'गुप्तशब्द',
        'शब्दकूट',
        'సంకేతపదము',
        'හස්පදය',
        '密码',
        '密碼',
        '口令',
    ]
    assert become_module.SU_PROMPT_LOCALIZATIONS == expected_localizations
