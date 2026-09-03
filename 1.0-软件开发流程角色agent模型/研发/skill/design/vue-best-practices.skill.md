---
name: vue-best-practices
description: MUST be used for Vue.js tasks. Strongly recommends Composition API with `<script setup>` and TypeScript as the standard approach. Covers Vue 3, SSR, Volar, vue-tsc. Load for any Vue, .vue files, Vue Router, Pinia, or Vite with Vue work. ALWAYS use Composition API unless the project explicitly requires Options API.
license: MIT
metadata:
  author: github.com/vuejs-ai
  version: "18.0.0"
---

# Vue Best Practices Workflow

Use this skill as an instruction set. Follow the workflow in order unless the user explicitly asks for a different order.

## Core Principles
- **Keep state predictable:** one source of truth, derive everything else.
- **Make data flow explicit:** Props down, Events up for most cases.
- **Favor small, focused components:** easier to test, reuse, and maintain.
- **Avoid unnecessary re-renders:** use computed properties and watchers wisely.
- **Readability counts:** write clear, self-documenting code.

## 1) Confirm architecture before coding (required)

- Default stack: Vue 3 + Composition API + `<script setup lang="ts">`.
- If the project explicitly uses Options API, load `vue-options-api-best-practices` skill if available.
- If the project explicitly uses JSX, load `vue-jsx-best-practices` skill if available.

### 1.1 Must-read core references (required)

- Before implementing any Vue task, make sure to read and apply these core references:
  - `references/reactivity.md`
  - `references/sfc.md`
  - `references/component-data-flow.md`
  - `references/composables.md`
- Keep these references in active working context for the entire task, not only when a specific issue appears.

### 1.2 Plan component boundaries before coding (required)

Create a brief component map before implementation for any non-trivial feature.

- Define each component's single responsibility in one sentence.
- Keep entry/root and route-level view components as composition surfaces by default.
- Move feature UI and feature logic out of entry/root/view components unless the task is intentionally a tiny single-file demo.
- Define props/emits contracts for each child component in the map.
- Prefer a feature folder layout (`components/<feature>/...`, `composables/use<Feature>.ts`) when adding more than one component.

## 2) Apply essential Vue foundations (required)

These are essential, must-know foundations. Apply all of them in every Vue task using the core references already loaded in section `1.1`.

### Reactivity

- Must-read reference from `1.1`: reactivity <!-- TODO: references/reactivity.md 缺失 -->
- Keep source state minimal (`ref`/`reactive`), derive everything possible with `computed`.
- Use watchers for side effects if needed.
- Avoid recomputing expensive logic in templates.

### SFC structure and template safety

- Must-read reference from `1.1`: sfc <!-- TODO: references/sfc.md 缺失 -->
- Keep SFC sections in this order: `<script>` → `<template>` → `<style>`.
- Keep SFC responsibilities focused; split large components.
- Keep templates declarative; move branching/derivation to script.
- Apply Vue template safety rules (`v-html`, list rendering, conditional rendering choices).

### Keep components focused

Split a component when it has **more than one clear responsibility** (e.g. data orchestration + UI, or multiple independent UI sections).

- Prefer **smaller components + composables** over one “mega component”
- Move **UI sections** into child components (props in, events out).
- Move **state/side effects** into composables (`useXxx()`).

Apply objective split triggers. Split the component if **any** condition is true:

- It owns both orchestration/state and substantial presentational markup for multiple sections.
- It has 3+ distinct UI sections (for example: form, filters, list, footer/status).
- A template block is repeated or could become reusable (item rows, cards, list entries).

Entry/root and route view rule:

- Keep entry/root and route view components thin: app shell/layout, provider wiring, and feature composition.
- Do not place full feature implementations in entry/root/view components when those features contain independent parts.
- For CRUD/list features (todo, table, catalog, inbox), split at least into:
  - feature container component
  - input/form component
  - list (and/or item) component
  - footer/actions or filter/status component
- Allow a single-file implementation only for very small throwaway demos; if chosen, explicitly justify why splitting is unnecessary.

### Component data flow

- Must-read reference from `1.1`: component-data-flow <!-- TODO: references/component-data-flow.md 缺失 -->
- Use props down, events up as the primary model.
- Use `v-model` only for true two-way component contracts.
- Use provide/inject only for deep-tree dependencies or shared context.
- Keep contracts explicit and typed with `defineProps`, `defineEmits`, and `InjectionKey` as needed.

### Composables

- Must-read reference from `1.1`: composables <!-- TODO: references/composables.md 缺失 -->
- Extract logic into composables when it is reused, stateful, or side-effect heavy.
- Keep composable APIs small, typed, and predictable.
- Separate feature logic from presentational components.

## 3) Consider optional features only when requirements call for them

### 3.1 Standard optional features

Do not add these by default. Load the matching reference only when the requirement exists.

- Slots: parent needs to control child content/layout -> component-slots <!-- TODO: references/component-slots.md 缺失 -->
- Fallthrough attributes: wrapper/base components must forward attrs/events safely -> component-fallthrough-attrs <!-- TODO: references/component-fallthrough-attrs.md 缺失 -->
- Built-in component `<KeepAlive>` for stateful view caching -> component-keep-alive <!-- TODO: references/component-keep-alive.md 缺失 -->
- Built-in component `<Teleport>` for overlays/portals -> component-teleport <!-- TODO: references/component-teleport.md 缺失 -->
- Built-in component `<Suspense>` for async subtree fallback boundaries -> component-suspense <!-- TODO: references/component-suspense.md 缺失 -->
- Animation-related features: pick the simplest approach that matches the required motion behavior.
  - Built-in component `<Transition>` for enter/leave effects -> transition <!-- TODO: references/component-transition.md 缺失 -->
  - Built-in component `<TransitionGroup>` for animated list mutations -> transition-group <!-- TODO: references/component-transition-group.md 缺失 -->
  - Class-based animation for non-enter/leave effects -> animation-class-based-technique <!-- TODO: references/animation-class-based-technique.md 缺失 -->
  - State-driven animation for user-input-driven animation -> animation-state-driven-technique <!-- TODO: references/animation-state-driven-technique.md 缺失 -->

### 3.2 Less-common optional features

Use these only when there is explicit product or technical need.

- Directives: behavior is DOM-specific and not a good composable/component fit -> directives <!-- TODO: references/directives.md 缺失 -->
- Async components: heavy/rarely-used UI should be lazy loaded -> component-async <!-- TODO: references/component-async.md 缺失 -->
- Render functions only when templates cannot express the requirement -> render-functions <!-- TODO: references/render-functions.md 缺失 -->
- Plugins when behavior must be installed app-wide -> plugins <!-- TODO: references/plugins.md 缺失 -->
- State management patterns: app-wide shared state crosses feature boundaries -> state-management <!-- TODO: references/state-management.md 缺失 -->

## 4) Run performance optimization after behavior is correct

Performance work is a post-functionality pass. Do not optimize before core behavior is implemented and verified.

- Large list rendering bottlenecks -> perf-virtualize-large-lists <!-- TODO: references/perf-virtualize-large-lists.md 缺失 -->
- Static subtrees re-rendering unnecessarily -> perf-v-once-v-memo-directives <!-- TODO: references/perf-v-once-v-memo-directives.md 缺失 -->
- Over-abstraction in hot list paths -> perf-avoid-component-abstraction-in-lists <!-- TODO: references/perf-avoid-component-abstraction-in-lists.md 缺失 -->
- Expensive updates triggered too often -> updated-hook-performance <!-- TODO: references/updated-hook-performance.md 缺失 -->

## 5) Final self-check before finishing

- Core behavior works and matches requirements.
- All must-read references were read and applied.
- Reactivity model is minimal and predictable.
- SFC structure and template rules are followed.
- Components are focused and well-factored, splitting when needed.
- Entry/root and route view components remain composition surfaces unless there is an explicit small-demo exception.
- Component split decisions are explicit and defensible (responsibility boundaries are clear).
- Data flow contracts are explicit and typed.
- Composables are used where reuse/complexity justifies them.
- Moved state/side effects into composables if applicable
- Optional features are used only when requirements demand them.
- Performance changes were applied only after functionality was complete.
