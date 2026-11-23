# Flower Sales Engine — Playbook (v1)

**Goal:** Find UAE flower wholesalers → message them on WhatsApp → track every lead to a sale.
**Budget:** ~$50–60/month. **Tools:** Apify (leads) · Google Sheet (tracker) · AiSensy (WhatsApp).

---

## Part 1 — One-time setup (≈ 1–2 hours of your time, 3–7 days waiting for Meta)

| # | Step | Notes |
|---|---|---|
| 1 | **Buy a new UAE SIM** (du or e& prepaid is fine) | Do **not** install WhatsApp on it. The number must be free for the WhatsApp API. Keep the SIM: you need it to receive the verification code. |
| 2 | **Create a Meta Business account** at business.facebook.com | Use the **exact legal company name** from your trade license. Add business address and a simple email on your company domain if you have one. |
| 3 | **Sign up to AiSensy** (aisensy.com) → choose **Basic** plan | Confirm the current USD price on their page before paying. |
| 4 | In AiSensy click **"Apply for WhatsApp Business API"** | It walks you through: log in with Facebook → pick your Meta Business account → enter the new number → enter the SMS code. |
| 5 | **Display name**: your company name | Must match your brand/company, or Meta rejects it. |
| 6 | **Business verification** in Meta Business Settings → Security Center | Upload trade license. Takes 1–5 working days. You can start sending before this, with a lower daily limit (enough for us). |
| 7 | **Submit the 3 message templates** below in AiSensy → Templates | Category: **Marketing**. Approval usually takes minutes to 24h. |
| 8 | **Add the saved replies** below in AiSensy → Settings → Canned Messages | So you can answer in 1 click. |

---

## Part 2 — Getting leads (10 minutes, ~free)

Apify is a website that copies business listings from Google Maps into a spreadsheet (name, phone, area, rating). My cloud environment can't reach Google Maps directly, so you run it once:

1. Create a free account at **apify.com** (free tier includes ~$5 credit/month ≈ 1,000 leads).
2. Search the store for **"Google Maps Scraper"** (the official one by Apify / compass). Click **Try for free**.
3. Paste these search terms (one per line):
   ```
   flower wholesale Dubai
   flower wholesaler Dubai
   fresh flowers supplier Dubai
   flower market Al Awir
   flower wholesale Sharjah
   flower shop Sharjah
   florist Dubai
   ```
4. Set **max results per search: 100**. Click **Start**. Wait ~5 minutes.
5. **Export → Excel**. Copy name, phone, area, rating, Maps link into the **Leads** tab of `Lead_Tracker.xlsx`. Status = **New**.
6. Quick clean-up: delete rows with no mobile number, and obvious non-buyers. **Put wholesalers and big shops first.**

> Want me to do this part instead? Later, you can give me an Apify access key through a secure form and I'll pull and clean the list for you.

---

## Part 3 — Message templates (submit to Meta)

`{{1}}` = the shop's name. Fill in `[brackets]` before submitting.

**Template 1 — `intro_kenya_roses`** (Day 0)
> Hi {{1}}, this is [Your name] from [Company]. We import fresh roses directly from our partner farms in Kenya and supply wholesalers in Dubai and Sharjah. No middlemen, so you get fresher stock at a better price.
>
> Would you like this week's price list?
>
> Buttons: **[Yes, send prices]** **[Not now]**
> Footer: *Reply STOP to stop messages*

**Template 2 — `followup_1`** (Day 3, no reply)
> Hi {{1}}, quick follow-up. Our next shipment of Kenyan roses lands in Dubai this week. Shall I send you prices and available colours?
>
> Buttons: **[Yes, send prices]** **[Not now]**
> Footer: *Reply STOP to stop messages*

**Template 3 — `followup_2`** (Day 7, no reply, last message)
> Hi {{1}}, last message from me. If you ever want to compare prices on Kenyan roses, just reply here and I'll send the list. Wishing you a good season.
>
> Footer: *Reply STOP to stop messages*

**Rules that protect your number:** max 2 follow-ups · always honour STOP immediately (mark "Not Interested") · send in small batches (50/day in week 1) · message during business hours (Sat–Thu, 10am–6pm).

---

## Part 4 — Saved replies (I draft, you approve and send)

| Shortcut | Reply |
|---|---|
| `/prices` | Thanks {{name}}! Here is this week's price list: [attach PDF/image]. Prices are per [stem/box], delivered to your shop in [Dubai/Sharjah]. Which colours and quantities do you usually order? |
| `/delivery` | We receive shipments [X times a week] by air from Kenya. Delivery to your shop is [same day / next day] after landing. |
| `/moq` | Minimum order is [X boxes]. For your first order we can be flexible so you can test the quality. |
| `/sample` | Happy to send a sample so you can see the quality yourself. What's the best address and time for delivery? |
| `/payment` | For the first order we work on [cash on delivery / bank transfer]. After that, [terms]. |
| `/quality` | Our roses come directly from [farm/region] in Kenya, cut and shipped within [X] days. Head size [X] cm, stem length [X–X] cm. |
| `/notnow` | No problem at all, thanks for letting me know. I'll leave it here. If you ever need a backup supplier, just message me. |
| `/stop` | Understood, you won't receive more messages from us. Have a great day. |

*(The `[brackets]` are the business details we'll fill in together once the system is live.)*

---

## Part 5 — Daily routine (15–20 min)

1. **Morning:** open the tracker → filter **Action Today = SEND FOLLOW-UP** → send Template 2 or 3 from AiSensy → update Last Contact + Follow-ups Sent.
2. **New outreach:** pick 30–50 **New** leads → AiSensy **Broadcast** with Template 1 → mark them **Contacted** with today's date.
3. **Inbox:** reply to anyone who answered using saved replies → update **Status**.
4. **Friday:** check the **Dashboard** tab. The only number that matters at first is the **reply rate**. Under 10%? We change the first message.

---

## Roadmap (only after v1 works)
- **v2:** AI drafts replies for you to approve (needs a higher plan, ~$80–100/mo). Do it once you're closing deals.
- **v3:** AI replies on its own for simple questions. You only handle pricing and closing.
- **v4:** Auto-sync AiSensy ↔ tracker so status updates itself.
