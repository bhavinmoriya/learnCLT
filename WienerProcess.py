import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io

def brownian_motion(n_steps=1000, dt=0.01, sigma=1.0, x0=0.0):
    """Generate a simple 1D Brownian motion path."""
    dW = np.random.normal(0, np.sqrt(dt), n_steps)
    W = np.cumsum(np.concatenate([[x0], sigma * dW]))
    t = np.linspace(0, n_steps*dt, n_steps+1)
    return t, W

def plot_brownian(n_paths, t_max, dt, sigma):
    """Create matplotlib figure for Streamlit."""
    n_steps = int(t_max / dt)
    fig, ax = plt.subplots(figsize=(12, 8))
    
    for i in range(n_paths):
        t, path = brownian_motion(n_steps, dt, sigma)
        ax.plot(t, path, alpha=0.7, linewidth=2, 
                label=f'Path {i+1}' if i < 5 else "")
    
    ax.set_xlabel('Time')
    ax.set_ylabel('Position')
    ax.set_title(f'Brownian Motion Simulation ({n_paths} paths)')
    ax.grid(True, alpha=0.3)
    if n_paths <= 5:
        ax.legend()
    plt.tight_layout()
    return fig

# Streamlit app
st.set_page_config(page_title="Brownian Motion Simulator", layout="wide")
st.title("🌀 Brownian Motion (Wiener Process) Simulator")

# Sidebar controls
st.sidebar.header("Simulation Parameters")
n_paths = st.sidebar.slider("Number of paths", 1, 20, 5)
t_max = st.sidebar.slider("Total time", 1.0, 50.0, 10.0)
dt = st.sidebar.slider("Time step (dt)", 0.001, 0.1, 0.01, 0.001)
sigma = st.sidebar.slider("Volatility (σ)", 0.1, 5.0, 1.0, 0.1)

# Generate and display plot
if st.button("🎲 Generate Paths", type="primary"):
    fig = plot_brownian(n_paths, t_max, dt, sigma)
    st.pyplot(fig)
else:
    # Show default on load
    fig = plot_brownian(n_paths, t_max, dt, sigma)
    st.pyplot(fig)

# Stats sidebar
col1, col2 = st.sidebar.columns(2)
with col1:
    st.metric("Steps per path", int(t_max/dt))
with col2:
    st.metric("Total time", f"{t_max:.1f}")

st.sidebar.markdown("""
**Wiener Process Properties:**
- Starts at 0
- Independent increments  
- Normally distributed: $dW ∼ N(0, √dt)$
- Variance scales with time
""")
