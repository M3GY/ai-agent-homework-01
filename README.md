Môj prvý AI Agent: Ukážka volania nástrojov

Tento projekt je jednoduchou, no zároveň silnou ukážkou základného AI Agenta vytvoreného v Pythone. Bola to naša prvá domáca úloha v rámci kurzu AI Agents v Robot Dreams.

Skript demonštruje kľúčový koncept "volania nástrojov" ("function-calling"), pri ktorom má LLM prístup k externým nástrojom, aby prekonal svoje vlastné obmedzenia a vyriešil problémy, ktoré by sám nezvládol.

Cieľom tohto agenta je odpovedať na jednoduchú matematickú otázku položenú v prirodzenom jazyku (napr. "Koľko je 5 plus 7?"). Hoci by LLM mohol na túto otázku odpovedať priamo, tento projekt demonštruje vzor delegovania výpočtu na spoľahlivý externý nástroj – v tomto prípade na lokálnu Python funkciu.

Tento projekt slúži ako základný príklad cyklu **Úvaha -> Akcia -> Pozorovanie**, ktorý je základom všetkých komplexných systémov AI agentov.


Ako to funguje

Agent postupuje podľa viacstupňového procesu, aby dospel k finálnej odpovedi:

1.  **Počiatočná výzva (Prompt):** Skript odošle otázku používateľa a popis dostupnej Python funkcie (`add`) do OpenAI API (s použitím modelu `gpt-3.5-turbo`).
2.  **Úvaha a výber nástroja:** LLM analyzuje výzvu a rozpozná, že si vyžaduje matematický výpočet. Určí, že funkcia `add` je vhodným nástrojom na túto úlohu.
3.  **Inštrukcia na volanie nástroja:** Namiesto priamej odpovede model vráti špeciálnu správu "tool call", ktorou dáva skriptu pokyn, aby vykonal funkciu `add` s argumentmi `a=5` a `b=7`.
4.  **Lokálne vykonanie:** Python skript spracuje túto inštrukciu a spustí lokálnu funkciu `add(5, 7)`. Funkcia vráti výsledok: `12`.
5.  **Pozorovanie a finálna odpoveď:** Skript odošle výsledok vykonania nástroja späť do LLM v druhom volaní API. LLM teraz disponuje chýbajúcou informáciou a použije ju na vygenerovanie finálnej, ľudsky čitateľnej odpovede: "5 plus 7 sa rovná 12."

## Použité technológie

* **Jazyk:** Python 3
* **Kľúčová knižnica:** `openai`
* **Poskytovateľ LLM:** OpenAI API (`gpt-3.5-turbo`)

## Inštalácia a použitie

Ak chcete spustiť tento skript na vlastnom počítači, postupujte podľa nasledujúcich krokov:

### 1. Klonovanie repozitára

```bash
git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
cd your-repository-name
```
*(Nahraďte `your-username` a `your-repository-name` vašimi skutočnými údajmi z GitHubu.)*

### 2. Inštalácia závislostí

Jedinou požadovanou knižnicou je oficiálny Python balíček od OpenAI. Môžete ho nainštalovať pomocou pip:

```bash
pip install openai
```

### 3. Nastavenie API kľúča

Z bezpečnostných dôvodov je skript navrhnutý tak, aby načítal váš OpenAI API kľúč z premennej prostredia. **Nikdy nevkladajte váš kľúč priamo do kódu.**

**Ako nastaviť premennú prostredia:**

* **Na macOS/Linux:**
    ```bash
    export OPENAI_API_KEY='vas_tajny_kluc_sem'
    ```
* **Na Windows (príkazový riadok):**
    ```bash
    set OPENAI_API_KEY=vas_tajny_kluc_sem
    ```

* **Ak používate IDE ako PyCharm:** Premennú prostredia môžete nastaviť v "Run/Debug Configurations" pre daný skript.

### 4. Spustenie skriptu

Po dokončení inštalácie môžete skript spustiť:

```bash
python "Homework 01.py"
```

Skript vypíše do konzoly celý proces, od počiatočnej výzvy až po finálnu odpoveď od AI.
