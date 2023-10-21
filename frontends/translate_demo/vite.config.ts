import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react-swc";
import { nodePolyfills } from "vite-plugin-node-polyfills";
import topLevelAwait from "vite-plugin-top-level-await";
import wasm from "vite-plugin-wasm";
import { NodeGlobalsPolyfillPlugin } from "@esbuild-plugins/node-globals-polyfill";
import rollupNodePolyFill from "rollup-plugin-polyfill-node";

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  return {
    server: {
      proxy: {
        "/api": {
          target: env.VITE_AIM_URL,
          rewrite: (path) => path.replace(/^\/api/, ""),
          changeOrigin: true,
          secure: false,
        },
      },
      port: env.VITE_APP_PORT,
    },
    plugins: [react(), wasm(), topLevelAwait(), nodePolyfills()],
    base: "",
    optimizeDeps: {
      esbuildOptions: {
        // Node.js global to browser globalThis
        define: {
          global: "globalThis",
        },
        // Enable esbuild polyfill plugins
        plugins: [
          NodeGlobalsPolyfillPlugin({
            buffer: true,
            process: true,
          }),
          // NodeModulesPolyfillPlugin(),
        ],
      },
      // exclude: ["react-virtualized"],
      include: ["prop-types", "react-dom"],
    },
    build: {
      rollupOptions: {
        plugins: [rollupNodePolyFill()],
      },
    },
  };
});
