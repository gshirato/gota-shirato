<template>
    <div>
        <Header />
        <h2>My blog</h2>
        <nuxt/>
        <Footer />
    </div>
</template>

<script>
export default {
    name: 'blogLayout'
}
</script>

<style>
h1 {
    font-size: 40pt;
}

h2 {
    font-size: 24pt;
}
</style>