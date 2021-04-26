
describe('Print Nanny setup wizard', () => {
    const PRINT_NANNY_URL = Cypress.env('PRINT_NANNY_URL')
    const PRINT_NANNY_EMAIL = Cypress.env('PRINT_NANNY_EMAIL')
    const PRINT_NANNY_PASSWORD = Cypress.env('PRINT_NANNY_PASSWORD')
    const PRINT_NANNY_TOKEN = Cypress.env('PRINT_NANNY_TOKEN')
    const OCTOPRINT_URL = Cypress.env('OCTOPRINT_URL')

    it('Retrieves Print Nanny auth token', () => {
        cy.fetchPrintNannyToken(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD).then($token => assert.exists($token))
    })

    it('Runs Print Nanny setup wizard', () => {
        cy.visit(OCTOPRINT_URL)
        cy.octoprintLogin(PRINT_NANNY_EMAIL, PRINT_NANNY_PASSWORD)
        cy.get('#octoprint_nanny_wizard_basic #octoprint_nanny_settings_auth_token_basic').type(PRINT_NANNY_TOKEN)
        cy.get('#octoprint_nanny_wizard_basic #octoprint_nanny_test_auth_token').click()
            .find('.alert').should('have.class', 'alert-success')

    })
})