import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from scipy.stats import norm

def simulate_clt_with_coin_flips(n, num_simulations=10000):
    # Simulate num_simulations trials of n coin flips
    trials = np.random.binomial(n, 0.5, num_simulations)

    # Calculate mean and standard deviation
    mean = np.mean(trials)
    std_dev = np.std(trials)

    return trials, mean, std_dev

def plot_results(trials, mean, std_dev, n, num_simulations):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot histogram
    ax.hist(trials, bins=20, density=True, alpha=0.6, color='g', label='Simulation')

    # Plot normal distribution curve
    x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    ax.plot(x, norm.pdf(x, mean, std_dev), 'r-', lw=2, label='Normal Distribution')

    ax.set_title(f'CLT: Number of Heads in {n} Coin Flips\n(Simulated {num_simulations} Trials)')
    ax.set_xlabel('Number of Heads')
    ax.set_ylabel('Density')
    ax.legend()
    ax.grid(True)

    return fig

def main():
    st.title("Central Limit Theorem (CLT) with Coin Flips")
    st.write("This app simulates the CLT by flipping a fair coin multiple times and plotting the distribution of the number of heads.")

    # User inputs
    n = st.slider("Number of coin flips per trial (n):", min_value=10, max_value=1000, value=50, step=10)
    num_simulations = st.slider("Number of trials to simulate:", min_value=1000, max_value=50000, value=10000, step=1000)

    # Simulate and plot
    if st.button("Run Simulation"):
        with st.spinner("Simulating..."):
            trials, mean, std_dev = simulate_clt_with_coin_flips(n, num_simulations)
            fig = plot_results(trials, mean, std_dev, n, num_simulations)
            st.pyplot(fig)

            st.write(f"**Mean number of heads:** {mean:.2f}")
            st.write(f"**Standard deviation:** {std_dev:.2f}")

if __name__ == "__main__":
    main()
