import os
import csv
import random

def generate_sample_dataset(output_dir="c:/CSEN/project/fake-news-detection/backend/dataset"):
    os.makedirs(output_dir, exist_ok=True)
    
    fake_samples = [
        "BREAKING: Secret Alien Technology Discovered in Underground Bunker! Government Hiding The Truth From Citizens! Scientists Shocked!",
        "SHOCKING: Drinking Lemon Juice Mixed With Miracle Powder Cures All Incurable Diseases Overnight, Doctors Don't Want You To Know!",
        "LEAKED DOCUMENT: Billionaires Plan To Teleport Moon To Another Galaxy Next Month Using Quantum Magnetism!",
        "CONFIRMED: Eating Chocolate 10 Times A Day Reverses Aging Instantly According To Anonymous Unnamed Blogger!",
        "ALERT: Invisible Robots Are Monitoring Your Thoughts Through Standard Household Mirrors! Share Before Deleted!",
        "EXCLUSIVE: Famous Celebrity Replaced By Hologram During Live Interview, Fans Notice Strange Glitch In Eyes!",
        "SCANDAL: Secret Society Controls Global Weather Patterns Using Giant Microwaves In The Arctic Circle!",
        "MIRACLE REMEDY: Ancient Tree Bark Powder Banishes Stress And Makes You Fly In Your Sleep!",
        "WARNING: Microwave Ovens Are Sending Secret Signals To Deep Space Satellites Without User Knowledge!",
        "UNBELIEVABLE: Local Man Discovers Free Unlimited Electricity Using Two Magnets And A Paperclip!"
    ]
    
    true_samples = [
        "WASHINGTON — The Federal Reserve announced a quarter-point interest rate adjustment following its policy meeting, citing inflation trends and employment data.",
        "GENEVA — The World Health Organization released updated global health guidelines recommending balanced diets and regular physical activity to reduce cardiovascular risks.",
        "TOKYO — Tech innovators unveiled a new semiconductor fabrication process designed to increase energy efficiency in data centers by twenty percent.",
        "LONDON — Researchers at Oxford University published findings in Nature Medicine analyzing the clinical efficacy of novel immunotherapies across five major hospital trials.",
        "PARIS — Representatives from 40 nations assembled for the International Climate Summit to outline binding commitments for reducing industrial emissions over the next decade.",
        "NEW YORK — Wall Street indexes closed moderately higher as earnings reports from major manufacturing and technology firms exceeded consensus analyst estimates.",
        "BERLIN — European aerospace consortium completed successful high-altitude test flights for hydrogen-powered zero-emission commercial flight prototypes.",
        "SYDNEY — Marine biologists documented significant coral regeneration across targeted sanctuary zones following intensive conservation management programs.",
        "BRUSSELS — The European Union passed comprehensive regulations standardizing consumer device charging ports across member states.",
        "TORONTO — Canadian research council announced major grant funding for renewable energy infrastructure and smart grid modernization projects."
    ]
    
    fake_titles = [
        "SHOCKING TRUTH REVEALED", "LEAKED REPORT PROVES CONSPIRACY", "DOCTORS HATE THIS SIMPLE TRICK",
        "SECRET GOVERNMENT PROJECT EXPOSED", "UNBELIEVABLE DISCOVERY CHANGES EVERYTHING",
        "CELEBRITY SCANDAL LEAKS ONLINE", "MIRACLE CURE SPREADING FAST", "WARNING TO ALL CITIZENS"
    ]
    
    true_titles = [
        "Official Statement Released by Ministry", "Economic Growth Indicators Show Stability",
        "Scientific Consensus Confirms Trial Results", "Central Bank Adjusts Key Financial Rates",
        "Global Summit Reaches Bilateral Accord", "Tech Firm Announces Quarterly Revenue Growth",
        "Environmental Protection Board Publishes Report", "University Study Validates Health Findings"
    ]

    fake_rows = []
    for i in range(300):
        t = fake_titles[i % len(fake_titles)] + ": " + fake_samples[i % len(fake_samples)]
        txt = fake_samples[i % len(fake_samples)] + f" Article ID #{i} claiming sensational facts without empirical verification or peer review. Click here to read more shocking evidence!"
        fake_rows.append({"title": t, "text": txt, "subject": "News", "date": "2026-01-01", "label": "1", "target": "FAKE"})

    true_rows = []
    for i in range(300):
        t = true_titles[i % len(true_titles)] + " - Official News"
        txt = true_samples[i % len(true_samples)] + f" Reporting according to official press release #{i}. Verified by independent Reuters standards and institutional statements."
        true_rows.append({"title": t, "text": txt, "subject": "politics", "date": "2026-01-01", "label": "0", "target": "REAL"})

    headers = ["title", "text", "subject", "date", "label", "target"]

    fake_path = os.path.join(output_dir, "Fake.csv")
    with open(fake_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(fake_rows)

    true_path = os.path.join(output_dir, "True.csv")
    with open(true_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(true_rows)

    combined_rows = fake_rows + true_rows
    random.seed(42)
    random.shuffle(combined_rows)

    train_path = os.path.join(output_dir, "train.csv")
    with open(train_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(combined_rows)

    print(f"✅ Generated dataset successfully ({len(combined_rows)} rows) at {output_dir}")

if __name__ == "__main__":
    generate_sample_dataset()
