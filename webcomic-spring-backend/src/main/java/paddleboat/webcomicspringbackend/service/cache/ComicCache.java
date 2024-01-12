package paddleboat.webcomicspringbackend.service.cache;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.lang.Nullable;
import org.springframework.stereotype.Service;
import paddleboat.webcomicspringbackend.global.Globals;
import paddleboat.webcomicspringbackend.model.PageIndex;
import paddleboat.webcomicspringbackend.model.entitiy.ComicChapter;
import paddleboat.webcomicspringbackend.model.entitiy.ComicPage;
import paddleboat.webcomicspringbackend.repository.ComicChapterRepository;
import paddleboat.webcomicspringbackend.repository.ComicPageRepository;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.List;

@Service
@RequiredArgsConstructor
@Slf4j
public class ComicCache {

    private final ComicPageRepository comicPageRepository;
    private final ComicChapterRepository comicChapterRepository;

    private LinkedHashMap<Integer, ComicChapter> chapterCache;

    /**
     * Loads the cache with active comic chapters and their respective pages.
     * If a chapter is active, it retrieves all pages for that chapter and maps them by page number.
     * The updated chapter cache is stored in the ComicCache class.
     */
    public int load() {
        try {
            LinkedHashMap<Integer, ComicChapter> newChapterCache = new LinkedHashMap<>();
            List<ComicChapter> chapters = comicChapterRepository.findByStatusCd(Globals.STATUS_ACTIVE);

            log.info("Loading Cache... Total chapters found: [{}]", chapters.size());


            // We need to set the previous and next chapters for each of these babies...
            // The following variable will be a huge helper for us
            ComicChapter previousChapter = null;
            for (ComicChapter chapter : chapters) {

                // This simple block here will setup our previous/next chapter references
                if (previousChapter != null) {
                    chapter.setPreviousChapter(previousChapter);
                    previousChapter.setNextChapter(chapter);
                }
                previousChapter = chapter;

                // If the chapter is active...
                if (chapter.getStatus().equals(Globals.STATUS_ACTIVE)) {

                    // Get all this chapter's pages...
                    List<ComicPage> pages = this.comicPageRepository.getPagesByChapterId(chapter.getChapterId());

                    LinkedHashMap<Integer, ComicPage> pageCache = new LinkedHashMap<>();

                    // Map them by page #...
                    for (ComicPage page : pages) {
                        page.setChapter(chapter);
                        pageCache.put(page.getPageNumber(), page);
                    }
                    chapter.setPages(pageCache);
                }

                newChapterCache.put(chapter.getChapterNumber(), chapter);
            }
            this.chapterCache = newChapterCache;

            // We return the total # of pages:
            int cacheCount = 0;
            for(ComicChapter chapter : chapterCache.values()) {

                if (chapter.getPages() == null) {
                    log.error("A chapter got initialized with a null page count! [chapter# {}]",
                            chapter.getChapterNumber());
                    throw new RuntimeException("Some chapter doesn't have pages!");
                }
                cacheCount += chapter.getPages().size();
            }
            return cacheCount;
        } catch (RuntimeException e) {
            log.error("Ran into exception initializing Comic Cache!!", e);
            throw e;
        }

    }

    /**
     * Retrieves the {@link ComicPage} corresponding to the given {@link PageIndex}.
     *
     * @param pageIndex the {@link PageIndex} representing the chapter number and the page number
     * @return the {@link ComicPage} corresponding to the given {@link PageIndex}, or null if not found
     * @throws RuntimeException if there is no page cache for the chapter
     */
    @Nullable
    public ComicPage getComicPage(PageIndex pageIndex) {
        ComicChapter chapter = this.chapterCache.get(pageIndex.getChapterNumber());
        HashMap<Integer, ComicPage> pages = chapter.getPages();

        if (pages == null) {
            log.error("No page cache for chapter number [{}]!!", chapter.getChapterNumber());
            throw new RuntimeException("No page cache for this chapter!");
        }

        return pages.get(pageIndex.getPageNumber());
    }

    @Nullable
    public ComicChapter getComicChapter(Integer chapterNumber) {
        return this.chapterCache.get(chapterNumber);
    }

    public List<ComicChapter> getAllChapters() {
        return this.chapterCache.values().stream().toList();
    }
}
