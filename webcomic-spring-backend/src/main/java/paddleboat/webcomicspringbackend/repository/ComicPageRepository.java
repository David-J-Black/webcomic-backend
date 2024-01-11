package paddleboat.webcomicspringbackend.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;
import paddleboat.webcomicspringbackend.model.entitiy.ComicPage;

import java.util.List;

@Repository
public interface ComicPageRepository  extends JpaRepository<ComicPage, Long> {

    @Query(value = "select  * from comic_page where page_number = :pageNumber and chapter_id = :chapterId and status='A'", nativeQuery = true)
    ComicPage getByPageNumAndChapterNum(@Param("pageNumber") final Long pageNumber,
                                               @Param("chapterId") final Long chapterId);

    @Query(value = "select  * from comic_page where chapter_id = :chapterId and status='A' order by page_number", nativeQuery = true)
    List<ComicPage> getPagesByChapterId(@Param("chapterId") final Long chapterId);

}
