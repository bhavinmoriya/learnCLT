import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")

st.set_page_config(page_title="Rabbit Walk Simulator")  # Unique browser tab title

st.title("🐰 Rabbit's Walk (2D Random Walk) Simulator")

# Sidebar controls for interactivity
st.sidebar.header("Simulation Controls")
steps = st.sidebar.slider("Number of Steps", min_value=100, max_value=5000, value=1000, step=100)
seed = st.sidebar.slider("Random Seed", min_value=0, max_value=100, value=42)

# Generate the random walk
np.random.seed(seed)
angles = 2 * np.pi * np.random.rand(steps)
steps_x = np.cos(angles)
steps_y = np.sin(angles)
positions_x = np.cumsum(steps_x)
positions_y = np.cumsum(steps_y)

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(positions_x, positions_y, marker='o', markersize=2, linestyle='-', linewidth=1, alpha=0.8, color='brown')
ax.set_title(f"Rabbit's Walk: {steps} Steps (Seed: {seed})", fontsize=16, fontweight='bold')
ax.set_xlabel("X Position", fontsize=12)
ax.set_ylabel("Y Position", fontsize=12)
ax.grid(True, alpha=0.3)
ax.axis('equal')

# Add start and end markers
ax.plot(0, 0, 'go', markersize=10, label='Start (Burrow)')
ax.plot(positions_x[-1], positions_y[-1], 'orange', marker='^', markersize=12, label='End')
ax.legend()

# Statistics
final_distance = np.sqrt(positions_x[-1]**2 + positions_y[-1]**2)
st.metric("Final Distance from Burrow", f"{final_distance:.1f} hops")

# Display the plot
st.pyplot(fig)

# Additional stats
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Hops", steps)
with col2:
    st.metric("Farthest X", f"{np.max(np.abs(positions_x)):.1f}")
with col3:
    st.metric("Farthest Y", f"{np.max(np.abs(positions_y)):.1f}")

st.info("🐇 Hop around! Adjust sliders to see the rabbit's random adventure change.")
