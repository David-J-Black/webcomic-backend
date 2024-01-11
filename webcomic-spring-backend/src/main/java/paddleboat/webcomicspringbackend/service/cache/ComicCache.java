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
import java.util.List;

@Service
@RequiredArgsConstructor
@Slf4j
public class ComicCache {

    private final ComicPageRepository comicPageRepository;
    private final ComicChapterRepository comicChapterRepository;

    private HashMap<Integer, ComicChapter> chapterCache;

    /**
     * Loads the cache with active comic chapters and their respective pages.
     * If a chapter is active, it retrieves all pages for that chapter and maps them by page number.
     * The updated chapter cache is stored in the ComicCache class.
     *
     * @throws Exception if there is an exception while initializing the cache
     */
    public void load() {
        try {
            HashMap<Integer, ComicChapter> newChapterCache = new HashMap<>();
            List<ComicChapter> chapters = comicChapterRepository.findByStatusCd(Globals.STATUS_ACTIVE);

            log.debug("Loading Cache... Total chapters found: [{}]", chapters.size());
            for (ComicChapter chapter : chapters) {

                // If the chapter is active...
                if (chapter.getStatus().equals(Globals.STATUS_ACTIVE)) {

                    // Get all this chapter's pages...
                    List<ComicPage> pages = this.comicPageRepository.getPagesByChapterId(chapter.getChapterId());
                    HashMap<Integer, ComicPage> pageCache = new HashMap<>();

                    // Map them by page #...
                    for (ComicPage page : pages) {
                        pageCache.put(page.getPageNumber(), page);
                    }
                    chapter.setPages(pageCache);
                }

                newChapterCache.put(chapter.getChapterNumber(), chapter);
            }
            this.chapterCache = newChapterCache;
        } catch (Exception e) {
            log.error("Ran into exception initializing Comic Cache!!", e);
            throw e;
        }

    }

    @Nullable
    public ComicPage getPage(PageIndex pageIndex) throws Exception {
        ComicChapter chapter = this.chapterCache.get(pageIndex.getChapterNumber());
        HashMap<Integer, ComicPage> pages = chapter.getPages();

        if (pages == null) {
            log.error("No page cache for chapter number [{}]!!", chapter.getChapterNumber());
            throw new Exception("No page cache for this chapter!");
        }

        return pages.get(pageIndex.getPageNumber());
    }
}
