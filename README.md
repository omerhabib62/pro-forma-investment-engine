# Pro-Forma Real Estate Investment Calculator

A Python- and Pandas-powered Pro-Forma Investment Calculator designed to model real estate equity waterfalls, including IRR hurdles, MOIC tiers, and detailed cash-flow distributions. Ideal for underwriting, deal analysis, and investor reporting.


## 🏗 System Architecture

```mermaid
graph TD
    A[User / Client] -->|Input Financials| B(Streamlit UI);
    B -->|Send Parameters| C{Pandas Engine};
    C -->|Calculate Cash Flow| D[Waterfall Logic];
    C -->|Calculate Exit Value| E[MOIC Logic];
    D --> F[Dataframe];
    E --> F;
    F -->|Render| G[Interactive Charts];
    F -->|Export| H[PDF Proposal];
