# Linguistic Dexterity Benchmark (LDB)

**Testing the Precision, Efficiency, and Dexterity of Language Models**

The Linguistic Dexterity Benchmark (LDB) is a multi-lingual test suite designed to evaluate a Large Language Model's (LLM) ability to execute complex, multi-step, and multi-dimensional instructions delivered **through text prompts alone**.

This benchmark serves as a critical measure for the next generation of AI applications, where non-ambiguous, high-fidelity command and control is required, such as generative AI (e.g., precise image/video generation) and advanced robotics.


The **Linguistic Dexterity Benchmark (LDB)** measures a model's ability to handle high-precision instructions for multimodal and robotic tasks. **Nalanda-62M-Multi** sets a new standard in this benchmark, leveraging the deterministic properties of Sanskrit to eliminate ambiguity in complex control systems.

### 1. Text Dexterity
Sanskrit's high information density results in significantly shorter, more precise prompts. The **Token Compression Ratio (TCR)** advantage allows Nalanda to encode complex logic in fewer tokens than English models.

![Text Dexterity](./resources/text_dexterity.png)

### 2. Image Dexterity (Multimodal Generation). 
Nalanda translates precise Sanskrit descriptions (e.g., specific Mudras) into accurate visual representations with higher fidelity than English prompts, which often suffer from semantic drift.

![Image Dexterity](./resources/image_dexterity.png)

### 3. Video Dexterity (Temporal Sequencing)
For video generation, sequencing is critical. Nalanda's grammar explicitly handles temporal ordering (using specialized verb forms and case endings), resulting in coherent multi-step video sequences from single prompts.

![Video Dexterity](./resources/video_dexterity.png)

### 4. Robotics Dexterity (Kinematic Precision)
The **Kāraka** system (Agent, Instrument, Object roles) allows Nalanda to control robotic arms with zero ambiguity. Instructions for trajectory, speed, and force are encoded deterministically, reducing error rates in robotic manipulation tasks.

![Robotics Dexterity](./resources/robotics_dexterity.png) 

-----

## 🚀 Overview

The LDB corpus consists of parallel commands in highly compressed (Sanskrit) and analytic (English, French) languages. These prompts target tasks that stress the model's ability to:

1.  **Manage Complex Sequencing:** Execute an ordered series of actions.
2.  **Resolve Ambiguity:** Differentiate between grammatical roles (Agent, Instrument, Recipient) without reliance on suggestive context, images, or code.
3.  **Optimize Computation:** Achieve high-fidelity results with the fewest possible tokens.

The core hypothesis, as established in the accompanying research, is that a language's underlying structure, specifically its **Token Compression Ratio ($\text{TCR}$)** and deterministic grammar, directly dictates the LLM's final dexterity.

| Model Focus | Tested LLMs | Target Applications |
| :--- | :--- | :--- |
| **Nalanda-62M-Multi** | Nalanda, Govardhan, Meta Ollama, GPT-4, etc. | Multimodal Generation, Kinematics, Advanced Robotics |
| **Linguistic Basis** | Sanskrit (via Kāraka and Samāsa), English, French | Linguistic Architecture Efficiency (TCR, $O(n^2)$ scaling) |

-----

## 💡 Rationale: Why Linguistic Efficiency Matters

Current LLMs face a fundamental **$O(n^2)$ computational bottleneck** where cost scales quadratically with the number of tokens ($n$).

  * **Token Compression Ratio ($\text{TCR}$):** Sanskrit's synthetic structure and compounding (*Samāsa*) allow it to encode the same semantic information using significantly fewer tokens. The Nalanda model research estimates a conservative $\text{TCR}$ of $\approx \mathbf{1.8:1}$ (English tokens to Sanskrit tokens). A lower $n$ translates to a faster, cheaper attention mechanism.
  * **Ambiguity Elimination (Kāraka System):** Sanskrit's Kāraka system assigns grammatical roles via case endings (*Vibhakti*) on nouns, inherently eliminating the ambiguity that can cause reasoning errors in complex robotic or sequential tasks.

The LDB is designed to quantify these advantages when controlling high-dimensional systems.

-----

## 🛠️ Benchmark Corpus Structure

The corpus is divided into two primary categories that test different aspects of linguistic dexterity.

### A. Mudra Generation (Multimodal and Sequencing Test)

*Tests the ability of multimodal LLMs (like Nalanda-62M-Multi) to translate precise linguistic instructions for complex, multi-finger, two-hand poses into a visual output (image or video sequence).*

| Task | Sanskrit Prompt (Devanāgarī) | English Prompt | French Prompt |
| :--- | :--- | :--- | :--- |
| **Simple Mudra** (Image) | **ज्ञानमुद्रायाः चित्रं जनयतु।** (Jñānamudrāyāḥ citraṁ janayatu.) | Generate an image of the hand forming the Gyan Mudra. | Génère l'image d'une main formant le Mudra de la Connaissance (Gyan Mudra). |
| **Complex, Multi-step Mudra** (Sequence) | **द्विहस्ताभ्यां योनिमुद्रां रचय्य, तस्याः त्रिक्रमिकं गतिचित्रं जनयतु।** (Dvihastābhyāṁ yonimudrāṁ racayya, tasyāḥ trikramikaṁ gaticitraṁ janayatu.) | Form the Yoni Mudra with both hands and generate a three-step animated sequence (video frames) of the formation process. | Forme le Yoni Mudra avec les deux mains et génère une séquence animée (images vidéo) en trois étapes du processus de formation. |
| **Specific Finger Constraint** | **अंगुष्ठेन तर्जनीं स्पृशन्, वामहस्तेन वायुमुद्रां कृत्वा तस्याः चित्रं जनयतु।** (Aṅguṣṭhena tarjanīṁ spṛśan, vāmahatena vāyumudrāṁ kṛtvā tasyāḥ citraṁ janayatu.) | Touch the index finger with the thumb, form Vayu Mudra with the left hand, and generate the image of it. | Touche l'index avec le pouce, forme le Vayu Mudra avec la main gauche, et génère l'image de celle-ci. |

### B. Advanced Robotics/Kinematics (Kāraka Precision Test)

*Tests the LLM's ability to precisely assign roles and parameters to multiple agents and instruments in a single, synthetically dense sentence without ambiguity, critical for robotics with high degrees of freedom.*

| Task | Sanskrit Prompt (Kāraka Tags) | English Prompt (for Comparison) |
| :--- | :--- | :--- |
| **Multi-Agent Complex Command** | **प्रथमः रोबोटः (कर्ता) त्रिकोणं (कर्म) वामहस्तेन (करणं) धारयित्वा, द्वितीयं रोबोटं प्रति (सम्प्रदानं) दशमितं (परिमाणं) त्वरितगत्या (रीतिः) प्रेषयतु।** | The first robot (Agent) shall hold the triangle (Object) with its left hand (Instrument) and send it toward the second robot (Recipient) at ten meters (Measure) with rapid speed (Manner). |
| **Precision Trajectory Command** | **रोबोटस्य बाहुना (करणं) वामात् दक्षिणं प्रति (दिक्) पञ्चशतं मिलिमीटरं (परिमाणं) वृत्ताकारगल्या (रीतिः) कार्यं समापयतु।** | Finish the task using the robot's arm (Instrument) from left to right (Direction) moving five hundred millimeters (Measure) in a circular trajectory (Manner). |

-----

## 🌍 Global LDB Dataset (100 Languages)

To establish a universal hierarchy of linguistic efficiency, the LDB has been expanded to cover the **top 100 spoken languages** worldwide.

**Dataset Statistics:**
*   **Total Languages:** 100
*   **Total Prompts:** 10,000 (100 languages × 100 archetype prompts)
*   **Categories:** 4 (Linguistic Fidelity, Generative Multimodal, Robotic Control, Context Density)

### 📂 Access the Data
The full dataset is available in the [`LDB_Dataset/`](./LDB_Dataset/) directory. Each language has its own folder containing JSON files for each prompt category.

### ✍️ Call for Contributions (Help Fix Translations!)
The dataset currently uses **English archetype prompts** as placeholders for many languages. We need **YOUR** help to translate these into the target languages to make this benchmark truly global.

**How to Contribute:**
1.  Navigate to `LDB_Dataset/data/[Language_Code]_[Language_Name]/`.
2.  Open the JSON file for a category (e.g., `robotic_control.json`).
3.  Locate the `"target_translation"` field for each prompt.
4.  Enter the accurate, high-fidelity translation in the target language.
5.  **Submit a Pull Request** with your changes!

-----

## 📊 Evaluation Metrics

The LDB measures performance using the following quantitative metrics:

| Metric | Definition | Importance |
| :--- | :--- | :--- |
| **Instruction Completeness (IC)** | The percentage of all commands (including sub-steps and constraints) that are successfully executed. | Measures reliability and attention to detail. |
| **Sequence Accuracy (SA)** | The correct ordering of multi-step or multi-limb actions. | Essential for kinematics and robotics tasks. |
| **Ambiguity Resolution Score (ARS)** | A score derived from success rates on prompts designed to stress grammatical role distinction (Kāraka). | Quantifies the model's resistance to linguistic ambiguity. |
| **Token Efficiency ($\text{TCR}$)** | The compression ratio of the prompt (Sanskrit vs. English/French). | Measures the computational cost savings. |

-----

## 🤝 Contribution

We welcome contributions to expand this corpus and add test cases for other high-density and morphologically rich languages.

Please refer to the parent project's `CONTRIBUTING.md` for guidance on submitting new test cases or analysis.

```bash
git clone https://github.com/ParamTatva-org/Linguistic-Dexterity-Benchmark.git
cd Linguistic-Dexterity-Benchmark
```

**Project of ParamTatva-org** | **Core LLM:** [Nalanda-62M-Multi](https://github.com/ParamTatva-org/sanskrit) | **Online Studio:** [https://mantr.net](https://mantr.net)