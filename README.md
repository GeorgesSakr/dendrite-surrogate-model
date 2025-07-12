# Dendritic Solidification Surrogate Modeling

This project develops a machine learning-based surrogate model to predict dendritic growth patterns in solidification processes. Simulations are based on a phase-field model implemented in FiPy. Two datasets are included — generated on 100×100 and 250×250 grids — and surrogate models (e.g., CNNs, PINN, etc.) are trained on these outputs.

## 📁 Project Structure

```plaintext
├── PDE and Data Generation        # FiPy-based PDE solver and data generation pipeline.
├── Project Proposal.pdf           # Project overview and objectives.
├── data/                          # Contains raw simulation data (excluded from GitHub).
├── 250 by 250 final frame/        # Final experiments with 250×250 data.
├── 100 by 100 final frame/        # Earlier version with 100×100 grid (only considered for testing).
├── 250 by 250 all frames/         # Final experiments on full time-series data.
├── Final Report.pdf               # Final results and analysis.
├── Guide.txt                      # Overall aproach of the project
├── README.md                      # Project overview and instructions.
├── LICENSE                        # MIT license text

## Getting Started

Install requirements:
```bash
pip install fipy numpy
