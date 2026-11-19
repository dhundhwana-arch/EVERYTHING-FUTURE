# Multilingual Glossary & Translation-Ready Specification

**Primary Documentation Language:** Clear Technical English (ISO 639-1: `en`)  
**Last Verified:** 2026-11-19

## Translation-Ready Schema

To support global accessibility across India, Europe, Asia, Africa, and the Americas, domain glossaries can be extended using a standardized CSV/Markdown schema:

```csv
term_id,english_term,domain_id,definition_en,hi_transliteration,gu_term,fr_term,ja_term,verification_status
```

## Example Entries (Verified Core Terms)

| Term ID | English | Domain | Hindi (hi) | Gujarati (gu) | French (fr) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| AI-001 | Artificial Intelligence | 001 | कृत्रिम बुद्धिमत्ता | કૃત્રિમ બુદ્ધિમત્તા | Intelligence artificielle |
| SEMI-001 | Semiconductor | 009 | अर्धचालक | અર્ધવાહક | Semi-conducteur |
| SPACE-001 | Orbital Velocity | 015 | कक्षीय वेग | કક્ષીય વેગ | Vitesse orbitale |
| FUS-001 | Nuclear Fusion | 021 | नाभिकीय संलयन | ન્યુક્લિયર ફ્યુઝન | Fusion nucléaire |
| TRADE-001 | Bill of Lading | 049 | लदान पत्र | બિલ ઓફ લેડિંગ | Connaissement |

## Localization Guidelines
1. Preserve canonical English technical identifiers, SI units, chemical formulas, and ISO standard numbers verbatim.
2. Mark community translations as `PARTIALLY_VERIFIED` until reviewed by a domain-fluent native speaker.
