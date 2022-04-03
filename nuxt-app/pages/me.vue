<template>
  <section>
    <!-- TITLE -->
    <div class="flex justify-between items-center">
      <div class="bg-cover bg-no-repeat rounded-full h-24 w-24" style="background-image: url(con.png)"></div>

      <div class="grid justify-items-end">
        <h1 class="text-7xl font-extrabold">Gota Shirato</h1>
        <p class="text-xl mt-5">PhD Student @University of Bonn</p>
      </div>
    </div>
    <hr class="py-4">
    <!-- Education / Research -->
    <h2 class="headline">Education / Research</h2>
    <ol class="relative border-l ml-3 border-gray-200 dark:border-gray-700">                  
      <li class="mb-10 ml-4">
        <div class="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -left-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
        <time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">Sep. 2015 - Aug. 2017</time>
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Ecole Centrale de Nantes (France)</h3>
        <p class="mb-4 text-base font-normal text-gray-500 dark:text-gray-400">Double Degree Program in Virtual Reality. Augmented Reality using Image Processing (OpenCV), Real-time Computer Graphics and 3D Modeling (CAD)</p>
        <a href="#" class="inline-flex items-center py-2 px-4 text-sm font-medium text-gray-900 bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:outline-none focus:ring-gray-200 focus:text-blue-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-700">Learn more <svg class="ml-2 w-3 h-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg></a>
      </li>
      <li class="mb-10 ml-4">
        <div class="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -left-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
        <time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">Sep. 2017 - Sep. 2019</time>
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Keio Graduate School (Japan)</h3>
        <p class="text-base font-normal text-gray-500 dark:text-gray-400">Master's Student in Industrial Engineering & Management Sciences. Sports Statistics, Machine Learning, Analysis of soccer matches using the Voronoi diagram Master's thesis: ”A New Approach to Evaluate a Team's Structure in Football: Calculating the Spaces using Voronoi Diagram and Empty Circles”</p>
      </li>
      <li class="ml-4">
        <div class="absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -left-1.5 border border-white dark:border-gray-900 dark:bg-gray-700"></div>
        <time class="mb-1 text-sm font-normal leading-none text-gray-400 dark:text-gray-500">Oct. 2020 - Present</time>
        <h3 class="text-lg font-semibold text-gray-900 dark:text-white">University of Bonn (Germany)</h3>
        <p class="text-base font-normal text-gray-500 dark:text-gray-400">PhD in Computer Science.</p>
        <a href="#" class="inline-flex items-center py-2 px-4 text-sm font-medium text-gray-900 bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:outline-none focus:ring-gray-200 focus:text-blue-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-700">Learn more <svg class="ml-2 w-3 h-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg></a>
      </li>
    </ol>

    <hr class="py-4 mb-3">
    <!-- Articles -->
    <h2 class="headline">Articles</h2>
    <div class="grid sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-3 gap-2 content-start">
      <div class="rounded overflow-hidden shadow-lg">
        <img class="w-full" src="/footballista-data.jpg" alt="Article Thumbnail">
        <div class="px-6 py-4">
          <div class="font-bold text-xl mb-2">「データ×アカデミズム」新たな分析メソッドの可能性</div>
          <p class="text-gray-700 text-base">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus quia, nulla! Maiores et perferendis eaque, exercitationem praesentium nihil.
          </p>
        </div>
        <div class="px-6 pt-4 pb-2">
          <span class="tag-line">#Footballista</span>
          <span class="tag-line">#データ</span>
          <span class="tag-line">#アカデミズム</span>
          <span class="tag-line">無料記事</span>
          <span class="date">2019.10.10</span>
        </div>
      </div>

      <div class="rounded overflow-hidden shadow-lg">
        <img class="w-full" src="/footballista-soccer-rugby.jpg" alt="Article Thumbnail">
        <div class="px-6 py-4">
          <div class="font-bold text-xl mb-2">【対談】友井川拓×山口遼：サッカー＆ラグビー指導者が持つべき 「知識と経験のバランス」</div>
          <p class="text-gray-700 text-base">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus quia, nulla! Maiores et perferendis eaque, exercitationem praesentium nihil.
          </p>
        </div>
        <div class="px-6 pt-4 pb-2">
          <span class="tag-line">#Footballista</span>
          <span class="tag-line">#サッカー</span>
          <span class="tag-line">#ラグビー</span>
          <span class="tag-line">会員限定</span>
          <span>2021.06.30</span>
        </div>
      </div>

      <div class="rounded overflow-hidden shadow-lg">
        <img class="w-full" src="/footballista-team-koln.jpg" alt="Article Thumbnail">
        <div class="px-6 py-4">
          <div class="font-bold text-xl mb-2">「チーム・ケルン」の日本人アナリストが語る、U-19ブンデスリーガ廃止論争</div>
          <p class="text-gray-700 text-base">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Voluptatibus quia, nulla! Maiores et perferendis eaque, exercitationem praesentium nihil.
          </p>
        </div>
        <div class="px-6 pt-4 pb-2">
          <span class="tag-line">#Footballista</span>
          <span class="tag-line">#サッカー</span>
          <span class="tag-line">#ドイツ</span>
          <span class="tag-line">会員限定</span>
          <span>2022.03.06</span>
        </div>
      </div>
    </div>
    <hr class="py-4">
    <!-- Projects -->
    <h2 class="headline">Projects</h2>
  </section>


</template>

<script>

export default {
}
</script>

<style>

.career-learn-more {
  @apply inline-flex items-center py-2 px-4 text-sm font-medium text-gray-900 bg-white rounded-lg border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:outline-none focus:ring-gray-200 focus:text-blue-700;
}

.career-point {
  @apply absolute w-3 h-3 bg-gray-200 rounded-full mt-1.5 -left-1.5 border border-white;
}
.career-time {
  @apply block mb-2 text-sm font-normal leading-none text-gray-400;
}

.career-headline {
  @apply flex items-center mb-1 text-lg font-semibold text-gray-900;
}

.career-description {
  @apply mb-4 text-base font-normal text-gray-500;
}

.cereer-list-item {
  @apply mb-10 ml-6;
}

.tag-line {
  @apply inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2;
}

h2.headline {
  @apply text-2xl pb-1 border-b font-semibold;
}

</style>