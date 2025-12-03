# Pro-Forma Real Estate Investment Calculator

A Python- and Pandas-powered Pro-Forma Investment Calculator designed to model real estate equity waterfalls, including IRR hurdles, MOIC tiers, and detailed cash-flow distributions. Ideal for underwriting, deal analysis, and investor reporting.

---

## Quick Start (How to Run)

### Prerequisites
- Python 3.9+
- Pip

---

### Installation

1. **Clone the repo:**

```bash
git clone https://github.com/omerhabib62/pro-forma-investment-engine.git
cd pro-forma-investment-engine
```

2. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the Engine:**

```bash
streamlit run app.py
```

---

### Live Demo: [Click Here to View App](https://pro-forma-investment-engine.streamlit.app/)

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
