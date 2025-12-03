import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from scipy.stats import norm

def simulate_dice_rolls(n, num_simulations=10000):
    # Simulate num_simulations trials of n dice rolls
    trials = np.sum(np.random.randint(1, 7, size=(num_simulations, n)), axis=1)

    # Calculate mean and standard deviation
    mean = np.mean(trials)
    std_dev = np.std(trials)

    return trials, mean, std_dev

def plot_dice_results(trials, mean, std_dev, n, num_simulations):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot histogram
    ax.hist(trials, bins=20, density=True, alpha=0.6, color='b', label='Simulation')

    # Plot normal distribution curve
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    ax.plot(x, norm.pdf(x, mean, std_dev), 'r-', lw=2, label='Normal Distribution')

    ax.set_title(f'CLT: Sum of {n} Dice Rolls\n(Simulated {num_simulations} Trials)')
    ax.set_xlabel('Sum of Dice')
    ax.set_ylabel('Density')
    ax.legend()
    ax.grid(True)

    return fig

def main():
    st.title("Central Limit Theorem (CLT) with Dice Rolls")
    st.write("This app simulates the CLT by rolling a die multiple times and plotting the distribution of the sum.")

    # User inputs
    n = st.slider("Number of dice rolls per trial (n):", min_value=1, max_value=50, value=10, step=1)
    num_simulations = st.slider("Number of trials to simulate:", min_value=1000, max_value=50000, value=10000, step=1000)

    # Simulate and plot
    if st.button("Run Simulation"):
        with st.spinner("Simulating..."):
            trials, mean, std_dev = simulate_dice_rolls(n, num_simulations)
            fig = plot_dice_results(trials, mean, std_dev, n, num_simulations)
            st.pyplot(fig)

            st.write(f"**Mean sum of dice:** {mean:.2f}")
            st.write(f"**Standard deviation:** {std_dev:.2f}")

if __name__ == "__main__":
    main()
