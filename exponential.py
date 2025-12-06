import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from scipy.stats import norm, expon

def simulate_exponential_samples(n, num_simulations=10000, scale=1.0):
    # Simulate num_simulations trials of n exponential samples
    trials = np.sum(np.random.exponential(scale, size=(num_simulations, n)), axis=1)

    # Calculate mean and standard deviation
    mean = np.mean(trials)
    std_dev = np.std(trials)

    return trials, mean, std_dev

def plot_exponential_results(trials, mean, std_dev, n, num_simulations):
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # Plot histogram of a single exponential sample
    single_sample = np.random.exponential(scale=1.0, size=10000)
    ax[0].hist(single_sample, bins=30, density=True, alpha=0.6, color='purple', label='Exponential Distribution')
    x_single = np.linspace(0, 10, 1000)
    ax[0].plot(x_single, expon.pdf(x_single, scale=1.0), 'r-', lw=2, label='PDF')
    ax[0].set_title('Original Exponential Distribution')
    ax[0].set_xlabel('Value')
    ax[0].set_ylabel('Density')
    ax[0].legend()
    ax[0].grid(True)

    # Plot histogram of the sum of n exponential samples
    ax[1].hist(trials, bins=30, density=True, alpha=0.6, color='b', label='Simulation')
    x_sum = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
    ax[1].plot(x_sum, norm.pdf(x_sum, mean, std_dev), 'r-', lw=2, label='Normal Distribution')
    ax[1].set_title(f'CLT: Sum of {n} Exponential Samples\n(Simulated {num_simulations} Trials)')
    ax[1].set_xlabel('Sum of Samples')
    ax[1].set_ylabel('Density')
    ax[1].legend()
    ax[1].grid(True)

    return fig

def main():
    st.set_page_config(page_title="Central Limit Theorem (CLT) with Exponential Distribution")  # Unique browser tab title
    st.title("Central Limit Theorem (CLT) with Exponential Distribution")
    st.write("This app simulates the CLT by summing exponential random variables and plotting the distribution.")

    # User inputs
    n = st.slider("Number of exponential samples per trial (n):", min_value=1, max_value=50, value=10, step=1)
    num_simulations = st.slider("Number of trials to simulate:", min_value=1000, max_value=50000, value=10000, step=1000)

    # Simulate and plot
    if st.button("Run Simulation"):
        with st.spinner("Simulating..."):
            trials, mean, std_dev = simulate_exponential_samples(n, num_simulations)
            fig = plot_exponential_results(trials, mean, std_dev, n, num_simulations)
            st.pyplot(fig)

            st.write(f"**Mean sum of samples:** {mean:.2f}")
            st.write(f"**Standard deviation:** {std_dev:.2f}")

if __name__ == "__main__":
    main()
