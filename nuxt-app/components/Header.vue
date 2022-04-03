<template>
    <section>
        <nav class="flex nav-bg">
            <div>
                <svg class="fill-current h-8 w-8 mr-2" width="54" height="54" viewBox="0 0 54 54" xmlns="http://www.w3.org/2000/svg"><path d="M13.5 22.1c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05zM0 38.3c1.8-7.2 6.3-10.8 13.5-10.8 10.8 0 12.15 8.1 17.55 9.45 3.6.9 6.75-.45 9.45-4.05-1.8 7.2-6.3 10.8-13.5 10.8-10.8 0-12.15-8.1-17.55-9.45-3.6-.9-6.75.45-9.45 4.05z"/></svg>
                <span class="font-semibold text-xl tracking-tight">Gota Shirato</span>
            </div>
            <div class="block lg:hidden">
                <button class="flex icon-button">
                    <svg class="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <title>Menu</title>
                    <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
                </button>
            </div>
            <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
                <div class="text-sm lg:flex-grow">
                    <nuxt-link to="/" class="header-item mr-4">Home</nuxt-link>
                    <nuxt-link to="/me" class="header-item mr-4">Me</nuxt-link>
                    <nuxt-link to="/topic" class="header-item">Topic</nuxt-link>
                </div>
                <div>
                    <nuxt-link to="#" class="download-button">Download</nuxt-link>
                </div>
            </div>
        </nav>

    </section>
</template>

<style>

.nav-bg {
    @apply items-center justify-between flex-wrap bg-indigo-400 p-6;
}

.header-item {
    @apply block mt-4 lg:inline-block lg:mt-0 text-indigo-50 hover:text-white;
} 

.icon-button {
    @apply items-center px-3 py-2 border rounded text-indigo-50 border-indigo-400 hover:text-white hover:border-white;
}

.download-button {
    @apply inline-block text-sm px-4 py-2 leading-none border rounded text-white border-white hover:border-transparent hover:text-indigo-500 hover:bg-white mt-4 lg:mt-0;
}
</style>
